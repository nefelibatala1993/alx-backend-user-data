#!/usr/bin/python3
"""Defines the BasicAuth class."""
import base64
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Defines the Basic Authentication Class"""
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Extracts the base64 part of a header."""
        if authorization_header is None or type(authorization_header) != str:
            return None
        
        if authorization_header[:6] != 'Basic ':
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """Decodes a base64 string."""
        if base64_authorization_header is None or type(base64_authorization_header) != str:
            return None
        
        try:
            decoded_string = base64.b64decode(base64_authorization_header)
        except ValueError:
            return None
        return decoded_string.decode('utf-8')
    
    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """Extract the users credentials from a decoded base64 string."""
        if decoded_base64_authorization_header is None or type(decoded_base64_authorization_header) != str:
            return None, None
        
        if ':' not in decoded_base64_authorization_header:
            return None, None
        return tuple(decoded_base64_authorization_header.split(':', 1))