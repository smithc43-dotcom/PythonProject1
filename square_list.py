# Name: Conner Smith
# Date: 2/23/26
# Project: square_list.py


def square_list(number_list):
    """
    Replaces each value in the given list with its square.
    The original list is modified. Nothing is returned.
    """

    index = 0

    while index < len(number_list):

        value = number_list[index]
        number_list[index] = value * value

        index += 1
