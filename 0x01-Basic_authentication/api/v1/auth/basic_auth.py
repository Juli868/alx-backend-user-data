#!/usr/bin/env python3
"""Authentication base."""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic authentication class."""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extract the encoded credentials."""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        result = authorization_header.split(' ')
        return result[1]
