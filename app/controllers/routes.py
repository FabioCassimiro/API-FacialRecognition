from app import app
from flask import request

from app.models import login
import os

@app.route('/teste',methods=['POST'])
def teste():
    print(request.form)
    if request.files:
        print('deu')
    return {'status':401}
    


@app.route("/facialrecognition", methods=['POST'])
def facial_recognition_login():
    result = login.valid_user(request.form, request.files)
    return result,200, {'Content-Type': 'application/json'}
