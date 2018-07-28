import os
from dotenv import load_dotenv
from app import create_app

# set env variable before app config
env = os.getenv('FLASK_ENV')
load_dotenv(os.path.join('instance/.env.' + env))

from config import app_config

app = create_app(app_config[env])

if __name__ == '__main__':
    app.run()
