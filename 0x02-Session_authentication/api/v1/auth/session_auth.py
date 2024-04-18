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
        session_id = uuid.uuid4()
        user_id_by_session_id = {seesion_id: userid}
        return session_id
