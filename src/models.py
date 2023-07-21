import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base, backref
from sqlalchemy import create_engine
from eralchemy2 import render_er

# Codigo desarrollado en equipo con Miguel Martin, Inti Luna y Christian Velasquez
Base = declarative_base()

favorites = Table('favorites',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('favorite_id', Integer, ForeignKey('favorite.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favorites = relationship('Favorite', secondary=favorites, lazy='subquery',
    backref=backref('users', lazy=True))

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    planets_id = Column(Integer, ForeignKey('planets.id'),
        nullable=False)
    characters_id = Column(Integer, ForeignKey('characters.id'),
        nullable=False)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'),
        nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    gravity = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    relationship('Favorite', backref='planets', lazy=True)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String, nullable=False)
    eye_color = Column(String(250), nullable=False)
    skin_color = Column(String, nullable=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    relationship('Favorite', backref='characters', lazy=True)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    model = Column(Integer, nullable=False)
    vehicle_class = Column(Integer, nullable=False)
    manufacturer = Column(Integer, nullable=False)
    cost_in_credits = Column(String(250), nullable=False)
    length = Column(Integer, nullable=False)
    crew = Column(String(250), nullable=False)
    passengers = Column(String(250), nullable=False)
    max_atmospheric_speed = Column(String(250), nullable=False)
    cargo_capacity = Column(String(250), nullable=False)
    consumables = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    relationship('Favorite', backref='vehicles', lazy=True)
    



# ------ MANY TO MANY RELATION --------
# tags = db.Table('tags',
#     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
#     db.Column('page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True)
# )

# class Page(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     tags = db.relationship('Tag', secondary=tags, lazy='subquery',
#         backref=db.backref('pages', lazy=True))

# class Tag(db.Model):
#     id = db.Column(db.Integer, primary_key=True)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')