from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_simple import JWTManager

import os
from config import app_config

ENV = os.getenv('FLASK_ENV')

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(app_config[ENV])
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)


# important to load the models after db init and migrate
from app import models

# import blueprint after models
from app.apis import blueprint as api
app.register_blueprint(api, url_prefix='/api')


@app.route('/')
def index():
    return 'Welcome!'
