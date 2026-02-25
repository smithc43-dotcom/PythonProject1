# Name: Conner Smith
# Date: 2/23/26
# Project: reverse_list.py


def reverse_list(value_list):
    """
    Reverses the elements in the list.
    """

    start = 0
    end = len(value_list) - 1

    while start < end:

        temp_value = value_list[start]
        value_list[start] = value_list[end]
        value_list[end] = temp_value

        start += 1
        end -= 1
