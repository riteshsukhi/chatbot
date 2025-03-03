import os
import openai
from fastapi import FastAPI

app = FastAPI()

# ✅ Root Route (Fix for 404 Not Found)
@app.get("/")
def home():
    return {"message": "Chatbot API is running!"}

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.get("/chat")
def chat(query: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": query}]
    )
    return {"response": response["choices"][0]["message"]["content"]}

