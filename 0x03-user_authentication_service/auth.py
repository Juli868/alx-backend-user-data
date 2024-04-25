#!/usr/bin/env python3
"""Transform data into usable data."""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Transform string password to encrypted bytes."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)
