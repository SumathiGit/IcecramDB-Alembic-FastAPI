from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
import os
from sqlalchemy.sql.sqltypes import String
from database import Base


class Branch(Base):
    __tablename__= 'branch'
    id = Column(Integer,primary_key = True)
    branchname = Column(String)
    address = Column(String)
    icecreams = relationship('Icecream', secondary = 'link')


class Icecream(Base):
    __tablename__ = 'icecream'
    id = Column(Integer, primary_key=True)
    icecreamname = Column(String)
    branches = relationship('Branch', secondary='link')

class Link(Base):
   __tablename__ = 'link'
   branch_id = Column(Integer, ForeignKey('branch.id'), primary_key = True)
   icecream_id = Column(Integer, ForeignKey('icecream.id'), primary_key = True)
