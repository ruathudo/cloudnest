import os
import pytest
from dotenv import load_dotenv

# load env variable before config
load_dotenv(os.path.join('../instance/.env.testing'))

from config import app_config
from app import create_app, db
from app.models import User


@pytest.fixture(scope='module')
def client():
    app = create_app(app_config['testing'])
    client = app.test_client()

    # Establish an application context before running the tests.
    with app.app_context():
        db.create_all()
        yield client
        db.drop_all()


@pytest.fixture(scope='module')
def first_user():
    # Insert user data
    user = User(first_name="First", last_name="User", username="user1", email='user1@gmail.com')

    db.session.add(user)
    db.session.commit()

    yield user

    db.session.rollback()


@pytest.fixture(scope='module')
def second_user():
    # Insert user data
    user = User(first_name="Second", last_name="User", username="user2", email='user2@gmail.com')

    db.session.add(user)
    db.session.commit()

    yield user

    db.session.rollback()
