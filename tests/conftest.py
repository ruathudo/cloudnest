import os
import pytest
from dotenv import load_dotenv

# load env variable before config
load_dotenv(os.path.join('../instance/.env.testing'))

from config import app_config
from app import create_app, db as _db
from app.models import User


@pytest.fixture(scope='module')
def app():
    return create_app(app_config['testing'])


@pytest.fixture(scope='module')
def client(app):
    client = app.test_client()

    # Establish an application context before running the tests.
    with app.app_context():
        yield client


@pytest.fixture(scope='module')
def db(app):
    with app.app_context():
        _db.create_all()

    yield _db
    _db.session.close()
    _db.drop_all()


@pytest.fixture(scope='module')
def first_user(db):
    # Insert user data
    user = User(first_name="First", last_name="User", username="user1", email='user1@example.com')

    db.session.add(user)
    db.session.commit()

    yield user


@pytest.fixture(scope='module')
def second_user(db):
    # Insert user data
    user = User(first_name="Second", last_name="User", username="user2", email='user2@example.com')

    db.session.add(user)
    db.session.commit()

    yield user
