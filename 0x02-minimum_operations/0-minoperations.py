#!/usr/bin/python3
"""Contains a function to solve Minimum Operations puzzle"""


def minOperations(n: int) -> int:
    """Given a text file with a single character `H`, and a text editor that
    can execute only two operations in this file: `Copy All` and `Paste`,
    calculates the fewest number of operations needed to result in exactly
    `n` number of `H` characters in the file.

    Args:
        n (int): number of `H` characters in the resulting text file.

    Returns:
        int: fewest number of operations needed. If n is impossible
            to achieve, returns `0`.
    """
    if type(n) != int or n <= 1:
        return 0

    """ if n = k * m for integers k & m, then to reach n, first: reach k,
    then do: one `copy all` and (m - 1) times `paste`. (k + (m - 1)*k = km = n)
    minOperations(k) to reach k, then (1 + (m-1)) = m operations to reach n
    minOperations(n) = minOperations(k) + m """

    # first find higest k (1 < k <= (n//2)) that satisfies n = k * m
    # start from n//2 and go down to find k
    k = n // 2
    while (k > 1):
        if n % k == 0:
            break
        k -= 1

    if k != 1:   # n = k * (n//k) & minOperations(n) = minOperations(k) + n//k
        return (minOperations(k) + n // k)

    # n is a prime number, miOperations(n) = miOperations(1) + n = n
    return (n)
