from datetime import datetime
from sqlalchemy import Column, String, Integer, Date, DateTime,ForeignKey, Sequence, Boolean, Text
from sqlalchemy.orm import relationship, synonym
from models.base import db
from models.base_model import BaseModel
from passlib.hash import pbkdf2_sha256


class User(BaseModel, db.Model):
    __tablename__ = 'user'
    # id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True, nullable=False)
    firstname = Column(String(200), nullable=False)
    lastname = Column(String(200))
    email = Column(String(200), nullable=False, unique=True)
    phone = Column(String(50), nullable=True)
    is_activated = Column(Boolean, default=False)
    activation_date = Column(DateTime)
    username = Column(String(500), nullable=False, unique=True)
    _password_hash = Column('password', String(2000), nullable=False)
    enabled = Column(Boolean, default=True)
    activation_token = Column(Text, nullable=False)
    creation_date = Column(DateTime, default=datetime.now())

    @property
    def password(self):
        return None

    @password.setter
    def password(self, val):
        if val is not None:
            self._password_hash = pbkdf2_sha256.hash(val)

    password = synonym('_password_hash', descriptor=password)

    def verify(self, _password):
        return pbkdf2_sha256.verify(_password, self._password_hash)
