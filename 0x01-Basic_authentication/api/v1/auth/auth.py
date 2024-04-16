#!/usr/bin/env python3
"""Deal with all authentication process and requirements."""
from flask import request
from typing import List, TypeVar


class Auth():
    """Authentication center."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Provide the credentials."""
        return False

    def authorization_header(self, request=None) -> str:
        """Provide the header with credentials."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Determine the current user."""
        return None
