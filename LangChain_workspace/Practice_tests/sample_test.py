from langchain_ollama import ChatOllama
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os


load = load_dotenv('./../.env')
print(os.environ.get('ANTHROPIC_API_KEY'))

llm = ChatOllama(
    
    model="llama3.1:latest", 
    base_url="http://localhost:11434",
    temperature=0.5
    )



llm_response = llm.invoke("Write a short poem about the ocean.")

print(llm_response.content)


#Loading 

