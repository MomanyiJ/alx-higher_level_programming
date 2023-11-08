#!/usr/bin/python3
"""Divides matrix"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number.

    Args:
    matrix: List of list of integers or floats.
    div: A number (integer or float) to divide matrix by

    Returns:
    New matrix with elemetns of input matrix divided by div
    and rounded to 2 decimal places

    Raises:
    TypeError: if matrix is not a matrix(list of lists) of integers/floats,
    or if div is not a number.
    TypeError: If each row of the matrix is not same size.
    ZeroDivisionError: if div is equal to 0.
    """
    new1 = []
    new2 = []
    if not matrix or type(matrix) != list:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    if not all(type(i) == list for i in matrix):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(element, (int, float))for i in matrix for element in i):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(j) == len(matrix[0]) for j in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        new1 = []
        for j in range(len(matrix[i])):
            new1.append(round(matrix[i][j] / div, 2))
        new2.append(new1)
    return new2
