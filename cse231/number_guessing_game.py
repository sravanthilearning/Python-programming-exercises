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

    :param number: int
    :return: boolean

    >>> is_good_number(12345)
    True
    >>> is_good_number(55432)
    False
    >>> is_good_number(444)
    False
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

    :return: tuple

    >>> report_results(54321, 12345)
    (5, 0)
    """
    return 5, 0
    pass


def player_progress(num_of_guesses, user_guess, correct_digits, correct_pos_digits):
    """
    Report the player's current progress.

    Nums of guesses, their guess, num of correct digits,
    and num of digits in the correct position.

    :param num_of_guesses: int
    :param user_guess: str
    :param correct_digits: int
    :param correct_pos_digits: int
    :return: str

    >>> player_progress(5, '12345', 4, 3)
    ------------------------------
    Used guesses: 5
    User guess: 12345
    Digits correct: 4
    Digits in correct position: 3
    ------------------------------
    """

    print('------------------------------')
    print('Used guesses: {}'.format(5))
    print('User guess: {}'.format('12345'))
    print('Digits correct: {}'.format(4))
    print('Digits in correct position: {}'.format(3))
    print('------------------------------')
    pass


if __name__ == '__main__':
    import doctest

    doctest.testmod()
