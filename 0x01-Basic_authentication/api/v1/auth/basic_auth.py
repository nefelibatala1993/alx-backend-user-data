#!/usr/bin/env python3
"""Defines the BasicAuth class"""
from api.v1.auth.auth import Auth
from models.user import User
import base64
from typing import TypeVar


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
        except Exception:
            return None
        return result_string

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
            ) -> (str, str):
        """Extracts user credentials from the decoded base64 string"""
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        user_creds = decoded_base64_authorization_header.split(':')
        if len(user_creds) == 1:
            return None, None

        email, password = user_creds
        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str
            ) -> TypeVar('User'):
        """Returns a User instance based on the email and password"""
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({"email": user_email})
        except Exception:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """Gets the user from the current request"""
        auth_header = self.authorization_header(request)
        if not auth_header:
            return None

        encoded = self.extract_base64_authorization_header(auth_header)
        if not encoded:
            return None

        decoded = self.decode_base64_authorization_header(encoded)
        if not decoded:
            return None

        email, pwd = self.extract_user_credentials(decoded)
        if not email or not pwd:
            return None

        user = self.user_object_from_credentials(email, pwd)
        return user
