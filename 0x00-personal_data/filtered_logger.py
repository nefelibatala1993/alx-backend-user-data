#!/usr/bin/env python3
"""Defines filter_datum function"""
import re
from typing import List


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> List[str]:
    """Returns the log message obfuscated"""
    for field in fields:
        match, replace = rf"{field}=.+?{separator}", f"{field}={redaction}{separator}"
        message = re.sub(match, replace, message)
    return message
