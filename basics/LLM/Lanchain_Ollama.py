from langchain_ollama import ChatOllama
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
# this is simple LLM application to do infrencing
llm = ChatOllama(
    model=os.getenv("LOCAL_OLLAMA_MODEL"), 
    base_url=os.getenv("LOCAL_OLLAMA_BASE_URL"),
    temperature=0.7,
    reasoning=False,
)

# print(llm.invoke("What is the capital of France?").content)