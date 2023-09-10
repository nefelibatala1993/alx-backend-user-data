#!/usr/bin/env python3
"""Defines the BasicAuth Class"""
import base64
import binascii
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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decodes the base64 authorization header to a normal string"""
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
        except binascii.Error as e:
            return None
        return decoded_bytes.decode('utf-8')
