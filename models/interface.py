from datetime import datetime
from sqlalchemy import Column, String, Integer, Date, DateTime, ForeignKey, Sequence, Boolean, Text
from sqlalchemy.orm import relationship, synonym
from models.base import db
from models.base_model import BaseModel


class Interface(BaseModel, db.Model):
    __tablename__ = 'interface'
    # id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    id = Column(Integer, Sequence('interface_id_seq'), primary_key=True, nullable=False)
    counterpart_id = Column(Integer, ForeignKey('counterpart.id'))
    interface_name = Column(String(255), nullable=False)
    description = Column(Text)
    counterpart_system_name = Column(String(255))
    request_data = Column(Text)
    response_data = Column(Text)
    direction_code = Column(Integer, nullable=False, default=0)
    method_code = Column(Integer, nullable=False, default=0)
    freq_code = Column(Integer, nullable=False, default=0)
    interface_status = Column(Integer, nullable=False, default=0)

    counterpart = relationship("Counterpart", foreign_keys='Interface.counterpart_id')
    interfaceItems = relationship('InterfaceItem', backref='Interface', lazy='dynamic')

