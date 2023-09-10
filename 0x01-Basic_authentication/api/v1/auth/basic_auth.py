#!/usr/bin/env python3
"""Defines the BasicAuth Class"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Defines the Basic Authentication Class"""
    def extract_base64_authorization_header(self, authorization_header: str) \
            -> str:
        """Extracts the base64 string from the authorization header"""
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        _list = authorization_header.split()
        if _list[0] != 'Basic':
            return None
        return _list[1]
