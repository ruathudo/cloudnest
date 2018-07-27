import os
from app import create_app


env = os.getenv('FLASK_ENV')

if __name__ == '__main__':
    app = create_app(env)
    app.run()
