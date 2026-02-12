# Name: Conner Smith
# Date: 02/11/2026
# Project: word_length_std_dev.py


def word_length_std_dev(text):
    """
    Calculate the sample standard deviation of the lengths of the words
    in the provided string. Words are assumed to be separated by spaces.
    """

    # Split text into words
    words = text.split()

    # Count the number of words
    num_words = len(words)

    # If there is only one word, the deviation is 0
    if num_words <= 1:
        return 0.0

    # Obtain the length of each word
    word_lengths = []
    for word in words:
        word_lengths.append(len(word))

    # Calculate the mean word length
    total_length = 0
    for length in word_lengths:
        total_length += length
    mean_length = total_length / num_words

    # Calculate the sum of squared differences
    squared_diff_sum = 0
    for length in word_lengths:
        squared_diff_sum += (length - mean_length) ** 2

    # Compute the sample standard deviation
    sample_std_dev = (squared_diff_sum / (num_words - 1)) ** 0.5
n
    return sample_std_dev
