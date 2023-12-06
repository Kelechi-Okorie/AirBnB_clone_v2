#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state', cascade='all, delete-orphan')
    if getenv('HBNB_TYPE_STORAGE') == 'file':
        @property
        def cities(self):
            """Getter attribute that returns list of City 
            instances with state_id equal to current State.id"""

            cities = [city for city in models.storage.all(City).values()
                      if city.state.id == self.id]
            return cities
