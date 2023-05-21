import os
from prompt_processor import PromptProcessor

input = "From custom text who is the hero?"
prompt_processor = PromptProcessor()
mode = prompt_processor.get_mode(input)
source = prompt_processor.get_source(input)
prompt = prompt_processor.get_prompt(input)
print('Input :', prompt)
process_action = prompt_processor.process_request(input)
print('Process Action :', process_action)