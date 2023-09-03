#!/usr/bin/env python3
"""Defines a function called filter_datum that returns a list of
obfuscated log messages."""
import logging
import re
import os
import mysql.connector
from mysql.connector.connection import MySQLConnection
from mysql.connector.connection import Error
from typing import List

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


# The first task
def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """redacts sensitive information from a message"""
    for field in fields:
        pattern = fr'({ field.strip() }=)([^{separator}]+){separator}'
        message = re.sub(pattern, r'\1' + redaction + separator, message)
    return message


# The Second Task
class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """Defines a custom formatter with the redacted value and
        the redactor and the separator"""
        msg = super(RedactingFormatter, self).format(record)
        redacted_msg = filter_datum(self.fields, self.REDACTION,
                                    msg, self.SEPARATOR)
        return redacted_msg


# The third task
def get_logger() -> logging.Logger:
    """Creates a custom logger with a"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # add the custom formatter
    formatter = RedactingFormatter(list(PII_FIELDS))
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    return logger


# Third task
def get_db() -> MySQLConnection | None:
    """returns a connector to the database"""
    hostname = os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost')
    username = os.environ.get('PERSONAL_DATA_DB_USERNAME', 'root')
    passwd = os.environ.get('PERSONAL_DATA_DB_PASSWORD', '')
    db = os.environ.get('PERSONAL_DATA_DB_NAME')

    try:
        connection = mysql.connector.connect(
            host=hostname,
            database=db,
            user=username,
            password=passwd
        )
    except Error as e:
        return None
    return connection
