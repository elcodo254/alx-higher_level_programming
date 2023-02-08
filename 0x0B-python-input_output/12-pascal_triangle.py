#!/usr/bin/python3
"""Defines a Pascal's Triang;e function"""


def pascal_triangle(n):
    """Reps Pascal triangle
    Returns a list of lists of integers
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        triangle = triangles[-1]
        tmp = [1]
        for i in range(len(triangle) - 1):
            tmp.append(triangle[i] + triangle[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
