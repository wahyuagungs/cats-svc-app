from datetime import datetime
from sqlalchemy import Column, String, Integer, Date, DateTime, Sequence, Boolean, Text
from sqlalchemy.orm import relationship, synonym
from models.base import db
from models.base_model import BaseModel


class Counterpart(BaseModel, db.Model):
    __tablename__ = 'counterpart'
    # id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    id = Column(Integer, Sequence('counterpart_id_seq'), primary_key=True, nullable=False)
    entity_name = Column(String(200), nullable=False)
    entity_abbrv = Column(String(50), nullable=False)
    institution_name = Column(String(255), nullable=True)
    institution_abbrv = Column(String(50), nullable=True)

    interfaces = relationship('Interface', backref='Counterpart', lazy='dynamic')

    def __init__(self, entity_name, entity_abbrv, institution_name, instituion_abbrv):
        self.entity_name = entity_name
        self.entity_abbrv = entity_abbrv
        self.institution_name = institution_name
        self.institution_abbrv = instituion_abbrv

