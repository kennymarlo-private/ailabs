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


class DataProcessor:
    
    NO_DEFINITVE_ANSWER = 'There is no definite answer to your inquiry as of the moment.'
    
    def processTextData(folder_name, file_name, input):
        try:
            data = DataLoader.load_data_file(folder_name, file_name)
            loader = UnstructuredFileLoader(data)
            documents = loader.load()
            persist_directory = 'db'
            
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
            split_texts = text_splitter.split_documents(documents)
            
            embeddings = OpenAIEmbeddings()
            vector_db = Chroma.from_documents(documents=split_texts, embeddings=embeddings, persist_directory=persist_directory)
            
            chat_model = ChatOpenAI(model_name="gpt-3.5-turbo-0301", temperature=0.9)
            qa = RetrievalQA.from_chain_type(llm=chat_model, chain_type="stuff", retriever=vector_db.as_retriever())
            response = qa.run(input)
            
            return response
        except Exception as e:
            return DataProcessor.NO_DEFINITVE_ANSWER  
            
    def processCSVData(folder_name, file_name, input):
        try:
            csv_data = DataLoader.load_data_file(folder_name, file_name)
            data = pd.read_csv(csv_data)
            
            pd_agent = create_pandas_dataframe_agent(OpenAI(temperature=0.9),data, verbose=True)
            response = pd_agent.run(input)
            
            return answer
        except Exception as e:
            return DataProcessor.NO_DEFINITVE_ANSWER