from datetime import datetime
from sqlalchemy import Column, String, Integer, Date, DateTime,ForeignKey, Sequence, Boolean, Text
from sqlalchemy.orm import relationship, synonym
from models.base import db
from models.base_model import BaseModel


class InterfaceItem(BaseModel, db.Model):
    __tablename__ = 'interface_item'
    # id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    id = Column(Integer, Sequence('interface_item_id_seq'), primary_key=True, nullable=False)
    interface_id = Column(Integer, ForeignKey('interface.id'))
    kd_module = Column(String(10), ForeignKey('module.kd_module'))
    kd_ctx_diagram = Column(String(255))

    interface = relationship("Interface", foreign_keys='InterfaceItem.interface_id')
    module = relationship("Module", foreign_keys='InterfaceItem.kd_module')
