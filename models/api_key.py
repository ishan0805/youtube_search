from datetime import datetime
from xmlrpc.client import Boolean
from sqlalchemy import Column, ForeignKey, Integer,String,DateTime ,Boolean
from sqlalchemy.orm import relationship

from database import Base

class ApiKey(Base):
    __tablename__ = "api_key"

    id = Column(Integer, primary_key=True, index=True)
    api_key=Column(String)
    create_time=Column(DateTime)
    active=Column(Boolean)
