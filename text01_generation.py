import os
from openai import OpenAI
from config import TEXT_MODEL,MAX_TOKENS
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("OPEN_AI_API_KEY")
client = OpenAI(api_key=API_KEY)

prompt = input("\n Enter your Question: ")

response = client.responses.create(
    model=TEXT_MODEL,
    instructions="You are a helpful AI assistant. Explain things in a clear and concise manner.",
    input=prompt,
    max_output_tokens=MAX_TOKENS
)
print(response.output_text)