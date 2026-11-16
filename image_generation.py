import os
import base64
from openai import OpenAI
from config import IMAGE_MODEL, IMAGE_QUALITY,IMAGE_SIZE,MAX_TOKENS
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("OPEN_AI_API_KEY")
client = OpenAI(api_key=API_KEY)

prompt = input("\n Describe the image you want to generate: ")

response = client.images.generate(
    model=IMAGE_MODEL,
    prompt=prompt,
    size=IMAGE_SIZE,
    quality=IMAGE_QUALITY,
    n=1)

print("openai response:",response)