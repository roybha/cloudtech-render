from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    data = request.get_json(silent=True) or {}
    name = data.get("name") or "World"
    return f"Hello, {escape(name)}!"
