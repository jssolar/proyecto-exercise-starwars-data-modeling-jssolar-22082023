import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    firt_name = Column(String(50), unique=True, nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    planet = relationship('Planet')
    Favorite = relationship('favorite')
    
    

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    name = Column(String(50))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    location = Column(String(50))
    moons = Column(String(50))
    suns = Column(String(50))
    population = Column(String(50))
    galaxi = Column(String(50))
  




class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    appearances = Column(String(100))
    Locations = Column(String(100), ForeignKey('planet.id'))
    Gender = Column(String(25))
    Dimensions = Column(String)
    Species = Column(String(50))
    Weapons = Column(String(50))
    Vehicles = Column(String(50))
    Character = relationship('character')
    
    
    






    def to_dict(self):
        return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
