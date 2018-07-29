from sqlalchemy.orm.exc import MultipleResultsFound
from sqlalchemy import or_
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
        result = User.query.filter(or_(User.id == id, User.username == username, User.email == email,
                                       User.username == email, User.email == username)).one_or_none()
    except MultipleResultsFound:
        logging.exception('DUPLICATE_USER')
        raise AppException('Internal Server Error', 500)

    return result
