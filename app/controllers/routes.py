from app import app
from app.models import login 
from flask import request

    


@app.route("/facialrecognition", methods=['POST'])
def facial_recognition_login():
    if login.valid_user(request.form):
        return {'authenticated':True},200, {'Content-Type': 'application/json'}
    else:
        return {'authenticated':False},401, {'Content-Type': 'application/json'}