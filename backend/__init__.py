from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route("/api/update", methods=["POST"])
def update():
    return jsonify({"name": "Alex"})