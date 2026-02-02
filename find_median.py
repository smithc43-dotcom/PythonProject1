# Name: Conner Smith
# Date: 02/01/2026
# Assignment: Project 5a – Find Median


def find_median(numbers):
    """
    Returns the statistical median of a list of numbers.
    """

    sorted_numbers = sorted(numbers)
    count = len(sorted_numbers)
    middle = count // 2

    if count % 2 == 1:
        return sorted_numbers[middle]
    else:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
