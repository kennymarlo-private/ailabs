import os 
from apikey import apikey
from generic_templates import create_generic_prompt_template
from conversation_buffer import create_conversation_buffer_memory
from llmchain import create_llmchain
from data_loader import DataLoader

import streamlit as st 
from langchain.llms import OpenAI
from langchain.agents import create_pandas_dataframe_agent


os.environ['OPENAI_API_KEY'] = apikey

# application aesthetics
st.title('Alpha One LLM')
prompt = st.text_input('Ask me something...') 

# llm templates
# _whoistemplate = create_generic_prompt_template()
# chat history for debugging
# _whoismemory = create_conversation_buffer_memory('name','chat_history')
# llm initialization
# llm = OpenAI(temperature=0.9, model_name="text-davinci-003", max_tokens=5)
# llm chaining
#_whoischain = create_llmchain(llm, _whoistemplate, True, 'name', _whoismemory)

# load CSV file
# loader = pd.read_csv('/home/deck/Documents/customllm/mockdata/MOCK_DATA.csv')

data_loader = DataLoader()
data = data_loader.load_data()

pd_agent = create_pandas_dataframe_agent(OpenAI(temperature=0),data, verbose=True)

# show results
if prompt: 
    #_whois = _whoischain.run(prompt)
    # st.write(_whois)
    # answer = lc.run(prompt)
    _answer = pd_agent.run(prompt)
    st.write(_answer)

    # with st.expander('Who is history'): 
    #    st.info(_whoismemory.buffer)