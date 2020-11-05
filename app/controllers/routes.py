from app import app
from flask import request
from app.models import login
import os

    


@app.route("/facialrecognition", methods=['POST'])
def facial_recognition_login():
    result = login.valid_user(request.form)
    return result,200, {'Content-Type': 'application/json'}
