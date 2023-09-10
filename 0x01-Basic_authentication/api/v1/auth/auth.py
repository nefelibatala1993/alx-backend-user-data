#!/usr/bin/env python3
"""Authentication for the API"""
from flask import request
from typing import List


class Auth:
    """Authentication class for authentication of users to the API"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require authentication for all routes except excluded_paths"""
        return False
    
    def authorization_header(self, request=None) -> str:
        """Return the value of the header request Authorization"""
        return None
    
    def current_user(self, request=None) -> str:
        """Returns the current use that is authenticated"""
        return None