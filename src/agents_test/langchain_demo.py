from os import getenv
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(override=True)


llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash")
response = llm.invoke("where is cairo located?")

print(response)
