#!/usr/bin/env python3
"""Defines a function called filter_datum that returns a list of
obfuscated log messages."""
import logging
import re
import os
import mysql.connector
from typing import List

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """redacts sensitive information from a message"""
    for field in fields:
        pattern = fr'({ field.strip() }=)([^{separator}]+){separator}'
        message = re.sub(pattern, r'\1' + redaction + separator, message)
    return message


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


def get_db() -> mysql.connector.connection.MYSQLConnection:
    """ Connection to MySQL environment """
    db_connect = mysql.connector.connect(
        user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        host=os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=os.getenv('PERSONAL_DATA_DB_NAME')
    )
    return db_connect


def main() -> None:
    """Obtain a database connection using get_db,
    retrieve all roles in the users table, and display
    each row under a formatted log message.
    """
    db = get_db()

    try:
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM users;")
            headers = [field[0] for field in cursor.description]

            logger = get_logger()

            for row in cursor:
                info_answer = ' '.join([f'{p}={f};' for f, p in zip(row, headers)])
                logger.info(info_answer)

    except mysql.connector.Error as err:
        # Handle database errors
        logger.error(f"Database error: {err}")

    finally:
        db.close()


if __name__ == "__main__":
    main()
