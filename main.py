
from dotenv import load_dotenv, find_dotenv
from deepeval import evaluate
from deepeval.metrics import AnswerRetrievalMetrics
from deepeval.test_cases import LLMTestCase

load_dotenv()

test_case = LLMTestCase(
    input="What is the capital of France?", 
    expected_output="The capital of France is Paris."
    actual_output="The capital of France is Paris."
)

evaluate(
             [test_case],
            metrics=[AnswerRetrievalMetrics()]
    
        )