#!/usr/bin/env python3
"""Deal with all authentication process and requirements."""
from flask import request
from typing import List, TypeVar


class Auth():
    """Authentication center."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determine if necessary to be logged in."""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        for checker in excluded_paths:
            if path.rstrip('/') == checker.rstrip('/'):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Provide the header with credentials."""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.header['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Determine the current user."""
        return None
