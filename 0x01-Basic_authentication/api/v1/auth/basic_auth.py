#!/usr/bin/env python3
"""Defines the BasicAuth class"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Definition for the Basic Authentication"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extract the base64 string from the authorization header"""
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        arr_header = authorization_header.split()
        if arr_header[0] != 'Basic':
            return

        return arr_header[1]
