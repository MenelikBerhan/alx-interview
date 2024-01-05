#!/usr/bin/python3
"""Contains Pascal Triangle generator function"""


def fact(num):
    """calculates a factorial of a number"""
    if num == 0 or num == 1:
        return 1
    res = 1
    while (num > 1):
        res *= num
        num -= 1
    return (res)


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal's triangle of `n`."""

    if n <= 0:
        return []
    pascal_triangle = []
    for row in range(n):
        row_list = []
        for k in range(row + 1):
            row_list.append(int(fact(row) / (fact(k) * fact(row - k))))
        pascal_triangle.append(row_list)

    return (pascal_triangle)


# based on Pascal’s Triangle Binomial Expansion
"""
Pascal's triangle defines the coefficients which appear in binomial expansions.
That means the nth row of Pascal's triangle comprises the coefficients of the
expanded expression of the polynomial (x + y)^n.

The expansion of (x + y)^n is:
(x + y)^n = a0x^n + a1x^(n-1)y + a2x^(n-2)y^2 + … + an-1xy^(n-1) + any^n

where the coefficients of the form ak (a0, a1 ... an) are precisely the numbers
in the nth row of Pascal's triangle. This can be expressed as:
    ak = (n k) = n!/(k! * (n-k)!)
"""
