#!/usr/bin/python3
"""The State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    if models.storage_t == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="states")
    else:
        name = ""

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """fs getter attribute that returns City instances"""
            values_city = models.storage.all("City").values()
            list_city = []
            for city in values_city:
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city
