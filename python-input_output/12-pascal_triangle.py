#!/usr/bin/python3

def pascal_triangle(n):
    triangle = []

    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            prev = triangle[-1]
            row = [1]

            for j in range(1, i):
                val = prev[j - 1] + prev[j]
                row.append(val)

            row.append(1)
            triangle.append(row)

    return triangle
