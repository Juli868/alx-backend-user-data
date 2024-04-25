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
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()
    def register_user(self, email: str, password: str) -> User:
        """Create a user with given credentials."""
        existing_user = self._db.find_user_by(email=email)
        if existing_user:
            raise ValueError("User <user's email> already exists")
        hashed_pwd = _hash_password(password)
        new_user = User(email, hashed_pwd)
        return new_user
