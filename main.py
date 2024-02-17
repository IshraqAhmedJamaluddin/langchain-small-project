import os
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

OPEN_AI_API_KEY = os.getenv('OPEN_AI_API_KEY')

llm = OpenAI(openai_api_key=OPEN_AI_API_KEY)

result = llm.invoke("Write a very short poem")

print(result)