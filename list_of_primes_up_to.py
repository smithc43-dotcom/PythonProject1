# Name: Conner Smith
# Date: 2/18/2026
# Project: list_of_primes_up_to.py

def list_of_primes_up_to(limit=100):
    """
    Returns a list of all prime numbers up to the given limit.
    """

    numbers = [True] * (limit + 1)

    numbers[0] = False
    numbers[1] = False

    num = 2

    while num <= limit ** 0.5:

        if numbers[num]:

            multiple = num * 2

            while multiple <= limit:
                numbers[multiple] = False
                multiple += num

        num += 1

    primes = []

    for i in range(len(numbers)):
        if numbers[i]:
            primes.append(i)

    return primes
