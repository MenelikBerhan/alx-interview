#!/usr/bin/python3
"""Contains a function to solve Minimum Operations puzzle"""


def minOperations(n: int, operations_dict: 'dict[int, int]' = {}) -> int:
    """Given a text file with a single character `H`, and a text editor that
    can execute only two operations in this file: `Copy All` and `Paste`,
    calculates the fewest number of operations needed to result in exactly
    `n` number of `H` characters in the file.

    Args:
        n: number of `H` characters in the resulting text file.
        operations_dict: dictionary to store already found minOperations
            from previous calls.

    Returns:
        int: fewest number of operations needed to result in exactly
            `n` number of `H` characters in the file. If n is impossible
            to achieve, returns `0`.
    """
    # print(f'Start: n={n}, dict: {operations_dict}')
    if type(n) != int or n <= 1:
        return 0

    if n in operations_dict:
        # print(f'returned from dict for n:{n}, {operations_dict}')
        return operations_dict[n]

    """ if n = k * m for integers k & m, then to reach n, first: reach k,
    then do: one `copy all` and (m - 1) times `paste`. (k + (m - 1)*k = km = n)
    minOperations(k) to reach k, then (1 + (m-1)) = m operations to reach n
    minOperations(n) = minOperations(k) + m """

    # first find higest k (1 < k < (n//2)) that satisfies n = k * m
    k = 2
    mid_n = n // 2
    k_max = 0       # highest divisor of n (less than half of n)
    while (k < mid_n):
        if n % k == 0:
            k_max = k
        k += 1

    # print(f'after loop: n={n}, kmax={k_max}')
    if k_max:
        minOperations_k = minOperations(k_max, operations_dict)
        operations_dict[n] = minOperations_k + n // k_max
        return (minOperations_k + n // k_max)

    # n is a prime number, miOperations(n) = miOperations(1) + n = n
    operations_dict[n] = n
    # print(f'END: at n={n}, {operations_dict}')
    return (n)
