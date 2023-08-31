#!/usr/bin/env python3
"""Defines a function called filter_datum that returns a list of
obfuscated log messages."""
import re


def filter_datum(fields, redaction, message, separator):
    """filters through a message that is supplied to it, and
    it redacts the associated field with it"""
    for field in fields:
        pattern = fr'({ field.strip() }=)([^{separator}]+){separator}'
        message = re.sub(pattern, r'\1' + redaction + separator, message)
    return message
