import os
import openai
from dotenv import load_dotenv
from openai.embeddings_utils import get_embedding
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base =  os.getenv("OPENAI_API_BASE")
openai.api_type = 'azure'
openai.api_version = '2022-12-01'

def get_database_answer(question):
    # question += "\n"
    response = ""
    prompt = ""
    # Insert code here
    return response, prompt