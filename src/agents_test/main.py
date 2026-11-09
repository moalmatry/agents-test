from openai import OpenAI
from dotenv import load_dotenv
from os import getenv

load_dotenv(override=True)
GEMINI_API_KEY = getenv("GOOGLE_API_KEY")
gemini = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)


def tell_me_a_joke():
    response = gemini.chat.completions.create(
        model="gemini-flash-lite-latest",
        messages=[
            {"role": "user", "content": "tell me a joke about software engineers"}
        ],
    )
    print(response.choices[0].message.content)


if __name__ == "__main__":
    tell_me_a_joke()
