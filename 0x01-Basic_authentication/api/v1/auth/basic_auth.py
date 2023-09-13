#!/usr/bin/env python3
"""Defines the BasicAuth Class"""
import base64
import binascii
from typing import TypeVar

from api.v1.auth.auth import Auth
from models.user import User


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

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Extracts user credentials from the decoded base64 authorization
        header"""
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(':')
        return (email, password)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Extracts user object from the credentials passed"""
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            search_result = User.search({'email': user_email})
        except Exception:
            return None

        if len(search_result) == 0:
            return None

        user = search_result[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user
