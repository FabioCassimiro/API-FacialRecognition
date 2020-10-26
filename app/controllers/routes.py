from app import app
from flask import request
from app.controllers.EncodesFace import facial_recognition
import os

app.config['imgdir'] = "./faces_request"


@app.route("/")
@app.route("/recognition",methods=['POST'])
def recognition():
    if request.files:
        file =request.files['image']
        filepath = os.path.join(app.config['imgdir'], file.filename);
        file.save(filepath)
    
    return facial_recognition(request.form['username'],file.filename)

