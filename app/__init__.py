from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restplus import Api
import os
from config import app_config

ENV = os.getenv('FLASK_ENV')

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(app_config[ENV])
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

# important to load the models after db init and migrate
from app import models


@app.route('/')
def index():
    return 'Welcome!'
