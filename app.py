import os
import sys
import streamlit as st
from apikey import apikey
from generic_templates import create_generic_prompt_template
from conversation_buffer import create_conversation_buffer_memory
from llmchain import create_llmchain
from data_loader import DataLoader
from data_processor import DataProcessor
from prompt_processor import PromptProcessor

api_key = os.environ['OPENAI_API_KEY'] = apikey

if not api_key:
    print("OPEN_API_KEY not found in the .env file")
    sys.exit(1)

st.title('ALPHA (Advanced LLM Processor for Human Assistance)')
input = st.text_input('Ask me something about...')

if len(input) > 0:
    prompt_processor = PromptProcessor()
    prompt = prompt_processor.get_prompt(input)
    print('Prompt: ', prompt)
    process_action = prompt_processor.process_request(input)
    print('Process action: ', process_action)
    match process_action:
        case 1:
            response = DataProcessor.process_csv_data('mockdata', 'test_data.csv', input)
        case 2:
            response = DataProcessor.process_text_data('mockdata', 'test_data.txt', input)
        case 3:
            res = DataProcessor.process_offline_data(input)
            response = res['result']
        case 4:
            res = DataProcessor.process_offline_data(input)
            response = res['result']
        case _default:
            response = 'It seems that my language model did not understand the context.'
else: 
    response = ''
if response is not None and len(response) > 0:  
    st.write(response)