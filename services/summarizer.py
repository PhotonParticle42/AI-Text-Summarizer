import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set")

client = OpenAI(api_key=api_key)


def build_prompt(text, mode):
    if mode == "short":
        instruction = "Summarize the following text in 2 to 3 short sentences."
    elif mode == "bullet":
        instruction = "Summarize the following text in 3 to 5 concise bullet points."
    elif mode == "paragraph":
        instruction = "Summarize the following text in one clear paragraph."
    else:
        instruction = "Summarize the following text clearly and concisely."

    return f"{instruction}\n\nText:\n{text}"


def generate_summary(text, mode):
    prompt = build_prompt(text, mode)

    response = client.responses.create(
        model="gpt-5",
        input=prompt,
    )

    return response.output_text