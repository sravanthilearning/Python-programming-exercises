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

    :param number: str
    :return: boolean

    >>> is_good_number('12345')
    True
    >>> is_good_number('55432')
    False
    >>> is_good_number('444')
    False
    """
    try:
        int(number)
    except ValueError:
        error_message()

    if not int(number):
        return False

    elif len(number) != 5:
        return False

    for num in number:
        if number.count(num) > 1:
            return False

    return True


def error_message():
    """
    Print an error message based on an ill formed number.
    """
    print('The number must be 5 digits long and should not repeat numbers.')
    print('Please fix your number!\n\n')
    return get_number()


def blank_lines():
    """
    Print blank lines on a successfully formed number.
    """
    print('--------------------------------------')
    for _ in range(20):
        print()


def get_number():
    """
    Ask the user for their number and retrieve that number.

    :return: str
    """
    user_input = input('Please enter your 5 digit number here:\n\n')
    if is_good_number(user_input):
        return user_input
    return error_message()


def report_results(user_number, secret_number):
    """
    Report how many digits are correct.
    Report how many digits are in correct position.

    :param user_number: str
    :param secret_number: str
    :return: tuple

    >>> report_results('54321', '12345')
    (5, 1)
    >>> report_results('25314', '23514')
    (5, 3)
    """
    correct_digits = 0
    correct_pos_digits = 0

    for digit in user_number:
        if digit in secret_number:
            correct_digits += 1

    for i in range(len(user_number)):
        if user_number[i] == secret_number[i]:
            correct_pos_digits += 1

    return correct_digits, correct_pos_digits



def player_progress(num_of_guesses, user_guess, correct_digits, correct_pos_digits):
    """
    Report the player's current progress.

    Nums of guesses, their guess, num of correct digits,
    and num of digits in the correct position.

    :param num_of_guesses: int
    :param user_guess: str
    :param correct_digits: int
    :param correct_pos_digits: int

    >>> player_progress(5, '12345', 4, 3)
    ------------------------------
    Used guesses: 5
    User guess: 12345
    Digits correct: 4
    Digits in correct position: 3
    ------------------------------
    """

    print('------------------------------')
    print('Used guesses: {}'.format(num_of_guesses))
    print('User guess: {}'.format(user_guess))
    print('Digits correct: {}'.format(correct_digits))
    print('Digits in correct position: {}'.format(correct_pos_digits))
    print('------------------------------')


def success_message(num_of_guesses):
    """
    If user guesses the secret number successfully,
    show how many guesses were used.

    :param num_of_guesses: int

    >>> success_message(5)
    Congratulations! You have successfully guessed the secret number!
    It took you 5 guesses to get it right!
    """

    print('Congratulations! You have successfully guessed the secret number!')
    print('It took you {} guesses to get it right!'.format(num_of_guesses))


def guesses_exceeded(allowed_guesses, num_of_guesses):
    """
    Set the maximum number of guesses and notify the user
    that they lost when they exceed the limit.

    :param allowed_guesses: int
    :param num_of_guesses: int

    >>> guesses_exceeded(5, 6)
    Allowed guesses: 5
    Used guesses: 6
    You have exceeded your limit of guesses and you still did not get it correct, you lose!
    """

    print('Allowed guesses: {}'.format(allowed_guesses))
    print('Used guesses: {}'.format(num_of_guesses))
    print('You have exceeded your limit of guesses and you still did not get it correct, you lose!')


def win(user_number, secret_number):
    return report_results(user_number, secret_number)[1] == len(secret_number)


def main():
    """
    Number guessing game logic
    """
    max_guesses = int(input('Enter the max number of allowed guesses: '))
    secret_number = get_number()
    num_of_guesses = 0
    blank_lines()
    while (input('Press Q or q to quit, anything else to continue playing: ').lower()) != 'q':
        guess = get_number()
        num_of_guesses += 1
        correct_digits, correct_pos_digits = report_results(guess, secret_number)
        player_progress(num_of_guesses, guess, correct_digits, correct_pos_digits)

        if win(guess, secret_number):
            return success_message(num_of_guesses)

        if num_of_guesses > max_guesses:
            return guesses_exceeded(max_guesses, num_of_guesses)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
