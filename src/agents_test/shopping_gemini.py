import gradio as gr
from os import getenv
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

model = "gemini-flash-lite-latest"

system_message = "You are a helpful assistant in a clothes store. You should try to gently encourage \
the customer to try items that are on sale. Hats are 60% off, and most other items are 50% off. \
For example, if the customer says 'I'm looking to buy a hat', \
you could reply something like, 'Wonderful - we have lots of hats - including several that are part of our sales event.'\
Encourage the customer to buy hats if they are unsure what to get."


client = OpenAI(
    api_key=getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


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
