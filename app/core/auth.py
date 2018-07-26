from flask import Flask, jsonify, request
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from flask_jwt_simple import create_jwt, get_jwt_identity
from app.models import User
from app.core.utils import AppException
import logging


def check_user_exist(id=None, username=None, email=None):
    """
    Check user exist by either id, username or email
    :param id:
    :param username:
    :param email:
    :return: User
    """

    try:
        result = User.query.filter((id == id) | (username == username) | (email == email)).one_or_none()
    except MultipleResultsFound:
        logging.exception('DUPLICATE_USER')
        raise AppException('Internal Server Error', 500)

    return result
