#!/usr/bin/env python3
"""Defines a function called filter_datum that returns a list of
obfuscated log messages."""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """redacts sensitive information from a message"""
    for field in fields:
        pattern = fr'({ field.strip() }=)([^{separator}]+){separator}'
        message = re.sub(pattern, r'\1' + redaction + separator, message)
    return message
