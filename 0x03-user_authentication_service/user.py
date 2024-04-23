#!/usr/bin/env python3
"""Define the user utilities."""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
Base = declarative_base()


class User(Base):
    """Table User definition."""

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250))
    hashed_password = Column(String(250))
    session_id = Column(String(250))
    reset_token = Column(String(250))
    next_id = 1

    def __init__(self, email: str, pwd: str):
        self.email = email
        self.hashed_password = pwd
        self.id = User.next_id
        User.next_id +=1
