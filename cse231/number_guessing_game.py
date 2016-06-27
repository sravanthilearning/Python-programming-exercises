"""
number_guessing_game.py

Author: Rafeh Qazi

Modified: June 2016

Copyright (C) 2016 Rafeh Qazi
"""


def is_good_number(number):
    """
    Let's a user know whether a number is properly formed.
    Each number should be 5 digits long and should not repeat numbers.

    >>> is_good_number(12345)
    True
    >>> is_good_number(55432)
    False
    >>> is_good_number(444)
    False

    :param number: int
    :return: boolean
    """
    if not number:
        return False
    if len(str(number)) != 5:
        return False
    for num in str(number):
        if str(number).count(num) > 1:
            return False
    return True


def error_message():
    """
    Print an error message based on an ill formed number.
    :return: str
    """
    pass


def blank_lines():
    """
    Print blank lines on a successfully formed number.
    :return: str
    """
    pass


def get_number():
    """
    Ask the user for their number.
    :return: str
    """
    pass


def report_results(user_number, secret_number):
    """
    Report how many digits are correct.
    Report how many digits are in correct position.

    >>> report_results(54321, 12345)
    'Digits correct: 5'
    'Digits in correct position: 0'

    :return: str
    """
    pass


if __name__ == '__main__':
    import doctest

    doctest.testmod()
