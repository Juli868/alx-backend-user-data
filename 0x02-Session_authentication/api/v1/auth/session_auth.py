#!/usr/bin/env python3
"""Authorize accordingly."""
from api.v1.auth.basic_auth import Auth
import uuid


class SessionAuth(Auth):
    """Authorizing according to the session."""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a session according to the user id."""
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id [session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Determine the user based on the session."""
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def session_cookie(self, request=None):
        """Define the cookie value."""
        if request is None:
            return None
        request.get(_my_session_id)
