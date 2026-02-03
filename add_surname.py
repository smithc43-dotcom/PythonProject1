# Name: Conner Smith
# Date: 10/__/2025
# Assignment: Project 5b

def add_surname(names):
    """
    Returns a list of names that start with 'K' with the surname 'Kardashian' added.
    """
    return [name + " Kardashian" for name in names if name.startswith("K")]
