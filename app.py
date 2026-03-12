from flask import Flask, jsonify, render_template, request

from services.summarizer import generate_summary

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Invalid request body."}), 400

    text = data.get("text", "").strip()
    mode = data.get("mode", "short").strip().lower()

    if not text:
        return jsonify({"error": "Please enter some text to summarize."}), 400

    allowed_modes = {"short", "bullet", "paragraph"}
    if mode not in allowed_modes:
        return jsonify({"error": "Invalid summary mode selected."}), 400

    try:
        summary = generate_summary(text, mode)
        return jsonify({"summary": summary})
    except Exception:
        return jsonify({"error": "Something went wrong while generating the summary."}), 500


if __name__ == "__main__":
    app.run(debug=True)