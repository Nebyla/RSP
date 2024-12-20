from typing import Dict, Any

from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import DateTime, String, Integer, BigInteger
from .model_extensions import ModelExtension
from datetime import datetime


class cars(ModelExtension):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    carsName = Column(String(255))
    dateRelease = Column(String(255))
    genre = Column(String(255))
    urlImage = Column(String(255))
    dateJoined = Column(DateTime, default=datetime.utcnow, nullable=False)
