from app import app
from flask import request
from app.controllers.EncodesFace import compara
import os
from werkzeug.utils import secure_filename

app.config['imgdir'] = "./face"


@app.route("/")
@app.route("/recognition",methods=['POST'])
def recognition():
    if request.files:
        file =request.files['image']
        filename = secure_filename(file.filename) # save file 
        filepath = os.path.join(app.config['imgdir'], filename);
        file.save(filepath)
    
    return compara(filename)
    
