from langchain.prompts import PromptTemplate

def create_generic_prompt_template():
    input_variables = ['name']
    template = 'Who is {name} using 5 words only'
    return PromptTemplate(input_variables=input_variables, template=template)