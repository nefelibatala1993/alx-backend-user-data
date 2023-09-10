#!/usr/bin/env python3
"""Authentication for the API"""
from flask import request
from typing import List


class Auth:
    """Authentication class for authentication of users to the API"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require authentication for all routes except excluded_paths"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        # make the path slash tolerant in the search
        if path[-1] != '/':
            path += '/'

        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Return the value of the header request Authorization"""
        if request is None or request.headers.get('Authorization') is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> str:
        """Returns the current use that is authenticated"""
        return None
