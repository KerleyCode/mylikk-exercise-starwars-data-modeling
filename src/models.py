import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

   
    followers = relationship("Followers", backref= "user_followers")
    favorites = relationship("Favorites", backref= "user_favorites")

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))

    characters = relationship("Favorites", backref='characters')
    planets = relationship("Favorites", backref= "planets")
    starships = relationship("Favorites", backref= 'starships')


class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(ForeignKey("user.id"))
    user_to_id = Column(ForeignKey("user.id"))
    

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(50))
    height = Column(Integer)
    mass = Column(Integer)
    
    favorite_id = Column(Integer, ForeignKey('favorites.id'))

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(50))
    orbital_period = Column(Integer)
    population = Column(Integer)

    favorite_id = Column(Integer, ForeignKey('favorites.id'))


class Starships(Base):

    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    starship_name = Column(String(50))
    manufacturer = Column(String(255))
    consumables = Column(Integer)
    
    favorite_id = Column(Integer, ForeignKey('favorites.id'))


    

    def to_dict(self):
        return {}


render_er(Base, 'diagram.png')
