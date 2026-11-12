import gradio as gr
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


message_input = gr.Textbox(
    placeholder="Enter your message", info="Enter message for gemini", lines=7
)
message_output = gr.Textbox(
    placeholder="Response from gemini", lines=7, info="Response from gemini"
)

view = gr.Interface(
    fn=message_gemini,
    title="Gemini",
    inputs=[message_input],
    outputs=[message_output],
    examples=["How are you today?", "where are you from "],
    flagging_mode="never",
)


view.launch()
