import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# Tabla de asociación para la relación muchos a muchos entre User, Planet y Character
user_planet_character_association = Table(
    'user_planet_character_association',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('planet_id', Integer, ForeignKey('planet.id')),
    Column('character_id', Integer, ForeignKey('character.id'))
)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
     # Relación muchos a muchos con Planet y Character a través de la tabla intermedia
    favorite_planets = relationship("Planet", secondary=user_planet_character_association, back_populates="favorited_by_users")
    favorite_characters = relationship("Character", secondary=user_planet_character_association, back_populates="favorited_by_users")


    
    # Relación uno a muchos con Personajes Favoritos
    favorite_characters = relationship("Character", secondary='favorite')

    # Relación uno a muchos con Planetas Favoritos
    favorite_planets = relationship("Planet", secondary='favorite')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
     # Relación inversa de muchos a muchos con User y Planet
    favorited_by_users = relationship("User", secondary=user_planet_character_association, back_populates="favorite_characters")
    favorite_planets = relationship("Planet", secondary=user_planet_character_association, back_populates="favorited_characters")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    location = Column(String(50))
    moons = Column(String(50))
    suns = Column(String(50))
    population = Column(String(50))
    galaxy = Column(String(50))
     # Relación inversa de muchos a muchos con User y Character
    favorited_by_users = relationship("User", secondary=user_planet_character_association, back_populates="favorite_planets")
    favorited_characters = relationship("Character", secondary=user_planet_character_association, back_populates="favorite_planets")

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_character = Column(Integer, ForeignKey('character.id'))
    user_planet = Column(Integer, ForeignKey('planet.id'))
    # Relación muchos a uno con User
    user = relationship(User)
    # Relación muchos a uno con Character
    character = relationship(Character)
    # Relación muchos a uno con Planet
    planet = relationship(Planet)

def to_dict(self):
    return {}

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')