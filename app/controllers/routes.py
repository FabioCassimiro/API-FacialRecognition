from app import app
from app.models import login 
from flask import request

    


@app.route("/facialrecognition", methods=['POST'])
def facial_recognition_login():
    if login.valid_user(request.form):
        return {'authenticated':True},{'Content-Type': 'application/json'}
    else:
        return {'authenticated':False},{'Content-Type': 'application/json'}