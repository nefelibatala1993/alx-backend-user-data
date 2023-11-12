#!/usr/bin/env python3
"""Defines the SessionAuth class"""
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """Defines the session authentication class that uses cookies"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session ID for a user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a User ID based on a Session ID"""
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Returns a User instance based on the cookie value"""
        if request is None:
            return None
        cookie_session_id = self.session_cookie(request)
        if cookie_session_id is None:
            return None

        user_id = self.user_id_for_session_id(cookie_session_id)
        if user_id is None:
            return None

        user = User.get(user_id)
        if user is None:
            return None
        return user
