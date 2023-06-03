# Graph tools import
from graph_tools import *

# Huggingface imports
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Environment variables
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# Load tokenizer of model
def load_tokenizer(model_name):
    return AutoTokenizer.from_pretrained(model_name)

# Load model from model_name
def load_model(model_name):
    return AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Generate text from model, tokenizer, and prompt
def generate(model, tokenizer, input_text):
    tokens = tokenizer(input_text, return_tensors="pt")
    tokens_out = model.generate(**tokens, max_new_tokens=100)
    output_text = str(tokenizer.batch_decode(tokens_out, skip_special_tokens=True))
    return output_text

# Create a conversation between two models
def conversation(model_name_1, model_name_2, initial_prompt=None, max_iter=20):
    model_1 = load_model(model_name_1)
    tokenizer_1 = load_tokenizer(model_name_1)
    model_2 = load_model(model_name_2)
    tokenizer_2 = load_tokenizer(model_name_2)
    
    if initial_prompt is None:
        initial_prompt = input("INITIAL PROMPT:")
    
    for _ in range(max_iter):
        new_prompt = generate(model_1, tokenizer_1, initial_prompt)
        print("MODEL 1:", new_prompt)
        initial_prompt = generate(model_2, tokenizer_2, new_prompt)
        print("Model 2:", initial_prompt)

# Test
model_name_1 = 'google/flan-t5-base'
model_name_2 = 'google/flan-t5-small'
initial_prompt = 'what is your name?'
conversation(model_name_1, model_name_2, initial_prompt=initial_prompt, max_iter=6)