import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

model = "gemini-flash-lite-latest"

client = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
system_message = "You are a helpful assistant that has been implemented by mohamed almatry based on google gemini model"


def chat(message, history):
    history = [{"role": h["role"], "content": h["content"]} for h in history]
    messages = (
        [{"role": "system", "content": system_message}]
        + history
        + [{"role": "user", "content": message}]
    )
    stream = client.chat.completions.create(model=model, messages=messages, stream=True)
    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ""
        yield response


gr.ChatInterface(fn=chat).launch()
