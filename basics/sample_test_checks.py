from deepeval.test_case import LLMTestCase;
from deepeval import evaluate;
from deepeval.metrics import AnswerRelevancyMetric
from dotenv import load_dotenv, find_dotenv
from deepeval.evaluate import AsyncConfig
from deepeval.models import OllamaModel
from LLM.Lanchain_Ollama import llm            # we are importing the llm object from Lanchain_Ollama.py
import os




ollama_model = OllamaModel(
    model="llama3.1:latest", 
    base_url="http://localhost:11434"
)


test_case = LLMTestCase(
    input="What is the capital of France?",
    expected_output="The capital of France is Paris.",
    actual_output=llm.invoke("What is the capital of France?").content
)

evaluate(test_cases =[test_case], 
         metrics = [AnswerRelevancyMetric(model=ollama_model)]
)
metric = AnswerRelevancyMetric(model=ollama_model)

metric.measure(test_case)

print("Score:", metric.score)
print("Success:", metric.success)
print("Threshold:", metric.threshold)
print("Reason:", metric.reason)

print("Actual Output:", test_case.actual_output)