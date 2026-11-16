import os
from openai import OpenAI
from config import TEXT_MODEL,MAX_TOKENS
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("OPEN_AI_API_KEY")
client = OpenAI(api_key=API_KEY)

prompt = input("\n Enter your Question: ")

stream = client.responses.create(
    model=TEXT_MODEL,
    instructions="You are a helpful AI assistant. Explain things in a clear and concise manner.",
    input=prompt,
    max_output_tokens=MAX_TOKENS,
    stream=True
)
print("openai response stream:",stream)
for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
    elif event.type == "response.completed":
        print("\n\nResponse completed.")
        print("Total tokens used:", event.response.usage.total_tokens)