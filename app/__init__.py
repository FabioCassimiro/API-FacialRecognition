from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
    r'/*':{
        "origins":"*"
    }
})

app.config.from_object('config')

from app.controllers import routes