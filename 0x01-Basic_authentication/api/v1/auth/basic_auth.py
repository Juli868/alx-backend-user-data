#!/usr/bin/env python3
"""Authentication base."""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar


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
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            primary = base64.b64decode(base64_authorization_header)
            res = primary.decode('utf-8')
            return res
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Determine the credential separately, i.e: username and password."""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        result = decoded_base64_authorization_header.split(':')
        return(str(result[0]), str(result[1]))

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Provode the credibility for the user, if exists in the db."""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieve the user instance for a request."""
        pass
