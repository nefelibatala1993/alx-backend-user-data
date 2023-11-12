#!/usr/bin/env python3
"""Defines the Auth class that handles the
the authentication of users for the api
"""
from os import getenv
from flask import request
from typing import List, TypeVar


class Auth:
    """Authentication class for users
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if the path requires authenication.
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[-1] != '/':
            path += '/'

        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Gets the authorization header from the request object
        """
        if request is None:
            return None

        authorization_header = request.headers.get('Authorization', None)
        if authorization_header is None:
            return None

        return authorization_header

    def current_user(self, request=None) -> TypeVar('User'):
        """Gets the current user that is authenticated
        """
        return None

    def session_cookie(self, request=None):
        """Returns a cookie value from a request"""
        if request is None:
            return None

        SESSION_NAME = getenv('SESSION_NAME', None)
        if SESSION_NAME is None:
            return None

        cookie = request.cookies.get(SESSION_NAME, None)
        if cookie is None:
            return None
        return cookie
