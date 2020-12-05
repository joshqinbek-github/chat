from flask import render_template, jsonify, request
from backend import app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route("/api/update", methods=["POST"])
def update():
    data = request.get_data()
    return jsonify({"name": data})