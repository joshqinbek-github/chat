from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route("/api/update", methods=["POST"])
def update():
    data = request.args.get("name")
    return jsonify({"name": data})