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
    firt_name = Column(String(50),  nullable=False)
    last_name = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(250), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)



class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    location = Column(String(50))
    moons = Column(String(50))
    suns = Column(String(50))
    population = Column(String(50))
    galaxi = Column(String(50))
    

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_character = Column(String, ForeignKey('character.id'))
    user_planet = Column(String, ForeignKey('planet.id'))
    user = relationship(User)
    

    def to_dict(self):
        return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')






