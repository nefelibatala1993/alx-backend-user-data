#!/usr/bin/env python3
"""Defines the class to manage authentication of API routes."""
from flask import request, Request
from typing import List, TypeVar


class Auth:
    """Manages API authentication."""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if a route requires authentication."""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        
        if path[-1] != '/':
            path += '/'
        
        for excluded_path in excluded_paths:
            if path == excluded_path:
                return False
        return True
    
    def authorization_header(self, request: Request = None) -> TypeVar('User'):
        """Checks if an authorization header is present and valid."""
        if request is None or request.headers.get('Authorization', None) is None:
            return None
    
        header: str = request.headers.get('Authorization', None)
        return header
    
    def current_user(self, request: Request = None) -> TypeVar('User'):
        return None
