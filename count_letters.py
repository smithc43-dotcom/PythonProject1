# Name: Conner Smith
# Date: 03/04/2026
# Project: count_letters.py

def count_letters(s):

    counts = {}

    s = s.upper()

    for letter in s:
        if letter.isalpha():
            counts[letter] = s.count(letter)

    return counts