#!/usr/bin/env python3
"""Defines the BasicAuth class"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """Definition for the Basic Authentication"""
    def extract_base64_authorization_header(
            self, authorization_header: str
            ) -> str:
        """Extract the base64 string from the authorization header"""
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        arr_header = authorization_header.split()
        if arr_header[0] != 'Basic':
            return
        return arr_header[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str
            ) -> str:
        """Decodes a base64 string if it is valid"""
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        result_string = ""
        try:
            result_bytes = base64.b64decode(base64_authorization_header)
            result_string = result_bytes.decode('utf-8')
        except base64.binascii.Error:
            return None
        return result_string
