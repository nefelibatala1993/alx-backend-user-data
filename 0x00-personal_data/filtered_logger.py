#!/usr/bin/env python3
"""Defines the filter_datum function"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Returns the log message obfuscated (the message argument
    that is passed as an argument)"""

    return ""