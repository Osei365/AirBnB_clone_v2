#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import place_amenity
from sqlalchemy import String, Column


class Amenity(BaseModel, Base):
    """Represents the alchemy class."""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
