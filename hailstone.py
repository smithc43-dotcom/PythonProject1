"""
Conner Smith
Date: 2026-01-28
Assignment: Project 4c - Hailstone Sequence
"""

def hailstone(start):
    """
    Calculates the number of steps in a hailstone sequence to reach 1.

    Parameters:
        start (int): Starting positive integer of the sequence

    Returns:
        int: Number of steps to reach 1
    """
    steps = 0
    n = start

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1

    return steps
