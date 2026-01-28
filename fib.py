# Conner Smith
# 2026-01-28
# Project 4b: Fibonacci Sequence Function

def fib(position):
    """
    Returns the Fibonacci number at the given position.

    Parameters:
        position (int): The position in the Fibonacci sequence (1-indexed)

    Returns:
        int: The Fibonacci number at that position
    """
    if position == 1 or position == 2:
        return 1

    previous = 1
    current = 1

    for _ in range(3, position + 1):
        next_value = previous + current
        previous = current
        current = next_value

    return current
