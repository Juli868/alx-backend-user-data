#!/usr/bin/env python3
"""Authentication base."""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decode a base64 header to find the credentials."""
        if base_64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            primary = base64.b64decode(base64_authorization_header)
            res = primary.decode('utf-8')
            return res
        except(TypeError, UnicodeDecodeError):
            return None
