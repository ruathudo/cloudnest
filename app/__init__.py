from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_simple import JWTManager
from flask_cors import CORS
from flask_rest_api import Api


# init 3rd party
db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()
migrate = Migrate()
rest = Api()


def create_app(configs):

    app = Flask('Cloud Nest')
    app.config.from_object(configs)
    CORS(app)

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    rest.init_app(app)

    # important to load the models after db init and migrate
    from app import models

    # import api endpoints to rest api
    from app.api import load_resources
    load_resources(rest)

    # register blueprint
    from app.core import core as core_blueprint
    app.register_blueprint(core_blueprint)

    @app.route('/')
    def index():
        return 'Welcome!'

    return app
