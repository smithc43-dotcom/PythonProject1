# Name: Conner Smith
# Date: 02/02/2026
# Assignment: Project 5c

def without_duplicates(original_list):
    """
    Returns a new list containing the same values as the original list,
    but with duplicates removed. The order of first appearance is preserved.
    """
    unique_list = []

    for value in original_list:
        if value not in unique_list:
            unique_list.append(value)

    return unique_list
 