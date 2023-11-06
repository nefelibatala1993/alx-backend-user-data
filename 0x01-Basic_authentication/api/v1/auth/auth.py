#!/usr/bin/env python3
"""Defines the Auth class that handles the
the authentication of users for the api
"""
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
        """Gets the authorization header from the request header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Gets the current user that is authenticated
        """
        return None
