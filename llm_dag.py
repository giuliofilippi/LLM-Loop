# Graph tools import
from graph_tools import *

# Environment variables
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# Huggingface imports
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model_name = 'google/flan-t5-base'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Langchain imports

# generate text from model
def generate(model,text):
    tokens = tokenizer(text, return_tensors="pt")
    tokens_out = model.generate(**tokens, max_new_tokens=100)
    text_out = str(tokenizer.batch_decode(tokens_out, skip_special_tokens=True))
    return text_out

# test
line = 'what is your name?'
print(generate(model=model,text=line))


