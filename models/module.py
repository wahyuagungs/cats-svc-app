from datetime import datetime
from sqlalchemy import Column, String, Integer, Date, DateTime, Sequence, Boolean, Text
from sqlalchemy.orm import relationship, synonym
from models.base import db
from models.base_model import BaseModel


class Module(BaseModel, db.Model):
    __tablename__ = 'module'
    kd_module = Column(String(10), primary_key=True, nullable=False)
    name = Column(String(200), nullable=False)
    module_abbrv = Column(String(50))

    InterfaceItems = relationship('InterfaceItem', backref='Module', lazy='dynamic')

    def __init__(self, kd_module, name, module_abbrv):
        self.kd_module = kd_module
        self.name = name
        self.module_abbrv = module_abbrv


