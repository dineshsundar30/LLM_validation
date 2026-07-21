from deepeval.test_case import LLMTestCase;
from deepeval import evaluate;
from deepeval.metrics import AnswerRelevancyMetric
from dotenv import load_dotenv, find_dotenv
from deepeval.evaluate import AsyncConfig
from deepeval.models import OllamaModel
import os

load_dotenv(find_dotenv())

ollama_model = OllamaModel(
    model="llama3.2:1b", 
    base_url="http://localhost:11434"
)

test_case = LLMTestCase(
    input="What is the capital of France?",
    expected_output="The capital of France is Paris.",
    actual_output="Chennai."
)

evaluate(test_cases =[test_case], 
         metrics = [AnswerRelevancyMetric(model=ollama_model)],
         async_config=AsyncConfig(run_async=False)
)