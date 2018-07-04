from app import db
from sqlalchemy import Column, Integer, String, DateTime


class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(100), unique=True)
    password = Column(String(100), nullable=True)
    email = Column(String(100), unique=True, nullable=False)
    avatar = Column(String(100), nullable=True)
    time_created = Column(DateTime(timezone=True), default=db.func.now())
    time_updated = Column(DateTime(timezone=True), default=db.func.now(), onupdate=db.func.now())

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name
