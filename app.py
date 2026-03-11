from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def fake_summary(text):
    text = text.strip()

    if len(text) <= 120:
        return text

    return text[:120] + "..."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    text = data.get("text", "")

    if not text.strip():
        return jsonify({"summary": "Please enter some text to summarize."})

    summary = fake_summary(text)
    return jsonify({"summary": summary})


if __name__ == "__main__":
    app.run(debug=True)