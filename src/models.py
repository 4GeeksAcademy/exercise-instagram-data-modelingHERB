import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()



class Register(Base):
    __tablename__ = 'register'
    age = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
   

class Login(Base):
    __tablename__ = 'login'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    content = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    content = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Share(Base):
    __tablename__ = 'share'
    messenger = Column(Integer, primary_key=True)
    twitter = Column(String(250), nullable=False)
    whatsapp = Column(String(250), nullable=False)
    facebook = Column(String(250), nullable=False)
    snapchat = Column(String(250), nullable=False)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e






    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
