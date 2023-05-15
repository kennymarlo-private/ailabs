from langchain.chains import LLMChain

def create_llmchain(llm,prompt,verbose,output_key,memory):
    llmchain = LLMChain(llm=llm, prompt=prompt, verbose=verbose, output_key=output_key, memory=memory)
    return llmchain