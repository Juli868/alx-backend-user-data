#!/usr/bin/env python3
"""DB module."""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:
    """DB class."""

    def __init__(self) -> None:
        """Initialize a new DB instance."""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object."""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Adding a user to the database."""
        new = User(email=email, pwd=hashed_password)
        self._session.add(new)
        self._session.commit()
        return new

    def find_user_by(self, **kwargs) -> User:
        """Find the user accornding to the dictionary provided."""
        if not kwargs:
            raise InvalidRequestError
        if not all(key in User.__table__.columns.keys() for key in kwargs):
             raise InvalidRequestError
         result = self._session.query(User).filter(**kwargs).first()
         if not result:
             raise NoResultFound
         return result
    
    def update_user(self, user_id: None, **kwargs):
        """Update the credentials."""
        user = self.find_user(id=user_id)
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user,value)
            else:
                raise ValueError
        self._session.commit()
