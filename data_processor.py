# This class invokes different fine tuning mechanism for the data set

from langchain.document_loaders.unstructured import UnstructuredFileLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
from data_loader import DataLoader
import pandas as pd
from dotenv import load_dotenv
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.vectorstores import Chroma
from langchain.llms import GPT4All, LlamaCpp
from constants import CHROMA_SETTINGS
import os

class DataProcessor:
    
    NO_DEFINITVE_ANSWER = 'There is no definite answer to your inquiry as of the moment.'
    
    def process_text_data(folder_name, file_name, input):
        try:
            data = DataLoader.load_data_file(folder_name, file_name)
            loader = UnstructuredFileLoader(data)
            documents = loader.load()
            persist_directory = 'db'
            
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
            split_texts = text_splitter.split_documents(documents)
            
            embeddings = OpenAIEmbeddings()
            vector_db = Chroma.from_documents(documents=split_texts, embeddings=embeddings, persist_directory=persist_directory)
            
            chat_model = ChatOpenAI(model_name="gpt-3.5-turbo-0301", temperature=0.9, verbose=True)
            qa = RetrievalQA.from_chain_type(llm=chat_model, chain_type="stuff", retriever=vector_db.as_retriever(), verbose=True)
            response = qa.run(input)
            
            return response
        except Exception as e:
            return DataProcessor.NO_DEFINITVE_ANSWER  
            
    def process_csv_data(folder_name, file_name, input):
        try:
            csv_data = DataLoader.load_data_file(folder_name, file_name)
            data = pd.read_csv(csv_data)
            
            pd_agent = create_pandas_dataframe_agent(OpenAI(temperature=0.9),data, verbose=True)
            response = pd_agent.run(input)
            
            return response
        except Exception as e:
            return DataProcessor.NO_DEFINITVE_ANSWER
        
        
    def process_offline_data(input):
        load_dotenv()
        
        embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME")
        persist_directory = os.environ.get('PERSIST_DIRECTORY')

        model_type = os.environ.get('MODEL_TYPE')
        model_path = os.environ.get('MODEL_PATH')
        model_n_ctx = os.environ.get('MODEL_N_CTX')
        embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
        db = Chroma(persist_directory=persist_directory, embedding_function=embeddings, client_settings=CHROMA_SETTINGS)
        retriever = db.as_retriever()
        callbacks = [StreamingStdOutCallbackHandler()]
        match model_type:
            case "LlamaCpp":
                llm = LlamaCpp(model_path=model_path, n_ctx=model_n_ctx, callbacks=callbacks, verbose=False)
            case "GPT4All":
                llm = GPT4All(model=model_path, n_ctx=model_n_ctx, backend='gptj', callbacks=callbacks, verbose=False)
            case _default:
                print(f"Model {model_type} not supported!")
                exit;
        qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True)
        result = qa(input)
        return result