from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_simple import JWTManager
from flask_cors import CORS
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec

import os
from config import app_config

ENV = os.getenv('FLASK_ENV')

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(app_config[ENV])
app.config.from_pyfile('config.py')
CORS(app)

db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)
docs = FlaskApiSpec(app)


# important to load the models after db init and migrate
from app import models

# import blueprint after models
from app.apis import api as api_blueprint
app.register_blueprint(api_blueprint)


@app.route('/')
def index():
    return 'Welcome!'
