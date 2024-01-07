#!/usr/bin/python3
"""Contains Pascal Triangle generator function"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal's triangle of `n`."""

    if n <= 0:
        return []
    pascal_triangle = []
    for row in range(n):
        row_list = []
        for k in range(row + 1):
            if k == 0 or k == row:
                row_list.append(1)
            else:
                # C(n, k) = C(n-1, k-1) + C(n-1, k)
                row_list.append(pascal_triangle[row - 1][k - 1] +
                                pascal_triangle[row - 1][k])
        pascal_triangle.append(row_list)

    return (pascal_triangle)


# based on Pascal’s Triangle Binomial Expansion
"""
Pascal's triangle defines the coefficients which appear in binomial expansions.
That means the nth row of Pascal's triangle comprises the coefficients of the
expanded expression of the polynomial (x + y)^n.

The expansion of (x + y)^n is:
(x + y)^n = a0 x^n + a1 x^(n-1)y + a2 x^(n-2)y^2 + … + an-1 xy^(n-1) + an y^n

where the coefficients of the form ak (a0, a1 ... an) are precisely the numbers
in the nth row of Pascal's triangle. This can be expressed as:
    ak = C(n, k) = n!/(k! * (n-k)!)

TO AVOID OVERFLOW ERROR when calculating factorial use:
    C(n, k) = C(n-1, k-1) + C(n-1, k)
"""
