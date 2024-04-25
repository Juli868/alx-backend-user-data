#!/usr/bin/env python3
"""Transform data into usable data."""
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Transform string password to encrypted bytes."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        """Initialise a class."""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Create a user with given credentials."""
        existing_user = self._db.find_user_by(email=email)
        try:
            if existing_user:
                raise ValueError(f"User {email} already exists")
            except NoResultFound:
                pass
        hashed_pwd = _hash_password(password)
        new_user = User(email, hashed_pwd)
        return new_user
    
    def valid_login(self, email: str, password: str) -> bool:
        """Check for the given credentials."""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        if (bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)):
            return True
        else:
            return False
