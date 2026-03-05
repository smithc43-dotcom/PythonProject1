# Name: Conner Smith
# Date: 03/04/2026
# Project: matrix_mult.py


def dot_prod(a, b):

    total = 0

    for i in range(len(a)):
        total = total + (a[i] * b[i])

    return total


def matrix_mult(A, B):

    if len(A[0]) != len(B):
        return None

    result = []

    for i in range(len(A)):

        row_result = []

        for j in range(len(B[0])):

            column = []

            for k in range(len(B)):
                column.append(B[k][j])

            value = dot_prod(A[i], column)

            row_result.append(value)

        result.append(row_result)

    return result