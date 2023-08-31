#!/usr/bin/env python3
"""Defines a function called filter_datum that returns a list of
obfuscated log messages."""
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str):
    ...
