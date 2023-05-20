import os
import sys
import time
from apikey import apikey
from generic_templates import create_generic_prompt_template
from conversation_buffer import create_conversation_buffer_memory
from llmchain import create_llmchain
from data_loader import DataLoader
from data_processor import DataProcessor
import pandas as pd

import streamlit as st 
from langchain.llms import OpenAI
from langchain.agents import create_pandas_dataframe_agent
from langchain.document_loaders.unstructured import UnstructuredFileLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI


api_key = os.environ['OPENAI_API_KEY'] = apikey

if not api_key:
    print("OPEN_API_KEY not found in the .env file")
    sys.exit(1)

# CLEANING OF PROMPT
# This will involve cleaning the prompts
# Scenarios
# Input should be "from {offline} {data}"
# where {offline/online} should be 'modes' and {data} should be 'source'
# The rest of the string input after should be regarded as input 
# triming the strings before passing the 'request' to the processors

# APPLICATION INPUT/REQUESTS
st.title('Alpha')
input = st.text_input('Ask me something about...') 


# <!--- ONLINE MODE --->
# This will involve invoking openai api



# [CSV] This will be on processing CSV files (with header using pandas)
response = DataProcessor.processCSVData('mockdata', 'test_data.csv', input)


# OFFLINE MODE
# This will be completely offline and uses maximum GPU power

# APPLICATION RESPONSE
# show results
if input: 
    #_whois = _whoischain.run(prompt)
    # st.write(_whois)
    # answer = lc.run(prompt)
    st.write(response)
     # st.write(bot_response)

    # with st.expander('Who is history'): 
    #    st.info(_whoismemory.buffer)