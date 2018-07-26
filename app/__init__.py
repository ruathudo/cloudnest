from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_simple import JWTManager
from flask_cors import CORS
from flask_rest_api import Api

import os
from config import app_config

ENV = os.getenv('FLASK_ENV')

app = Flask('Cloud Nest', instance_relative_config=True)
app.config.from_object(app_config[ENV])
app.config.from_pyfile('config.py')
CORS(app)

db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)
rest = Api(app)

# important to load the models after db init and migrate
from app import models

# import api endpoints to rest api
from app.api import load_resources
load_resources(rest)


@app.route('/')
def index():
    return 'Welcome!'
