# imports
from langchain.llms import OpenAI
from config import KEY

# generate response
def generate_response(input_text):
  '''
  input_text: str
  '''
  llm = OpenAI(temperature=0.7, openai_api_key=KEY)
  return llm