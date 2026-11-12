import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
model_name = "gemini-flash-lite-latest"
system_message = (
    "You are a helpful assistant that responds in markdown without code blocks"
)

message_input = gr.Textbox(
    label="Your message: ", info="Enter message for gemini", lines=7
)

message_output = gr.Markdown(label="Response")


def message_gemini(prompt):
    message = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]
    response = client.chat.completions.create(
        model="gemini-flash-lite-latest",
        messages=message,
    )
    return response.choices[0].message.content


def message_gemini(prompt):
    message = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]
    response = client.chat.completions.create(
        model="gemini-flash-lite-latest",
        messages=message,
    )
    return response.choices[0].message.content


def stream_gemini(prompt):
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt},
    ]
    stream = client.chat.completions.create(
        model=model_name, messages=messages, stream=True
    )
    result = ""
    for chunk in stream:
        result += chunk.choices[0].delta.content or ""
        yield result


view = gr.Interface(
    fn=stream_gemini,
    title="Gemini",
    inputs=[message_input],
    outputs=[message_output],
    examples=[
        "Explain the Transformers architecture to layperson",
        "Explain the Transformer architecture to an aspiring AI engineer",
    ],
    flagging_mode="never",
)
view.launch()
