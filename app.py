import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from openai import OpenAI

load_dotenv()

app = Flask(__name__)


api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set")

client = OpenAI(api_key=api_key)


def real_ai_summary(text):
    response = client.responses.create(
        model="gpt-5",
        input=(
            "Summarize the following text in 3 to 5 clear bullet points. "
            "Keep the meaning accurate and concise.\n\n"
            f"Text:\n{text}"
        ),
    )

    return response.output_text


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    text = data.get("text", "")

    if not text.strip():
        return jsonify({"summary": "Please enter some text to summarize."})

    try:
        summary = real_ai_summary(text)
        return jsonify({"summary": summary})
    except Exception as e:
        return jsonify({"summary": f"Error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)