from flask import request
from app import app

@app.route("/")
@app.route("/recognition")
def recognition():
    return "ok"