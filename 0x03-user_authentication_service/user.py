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
