#!/usr/bin/python3
"""Making Change puzzle solution
using GeeksforGeeks tutorials:
https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/
"""
# A Dynamic Programming based Python3 program to
# find minimum of coins to make a given change V
import sys


# m is size of coins array (number of
# different coins)
def makeChange(coins, total):
    """Finds the no. of coins needed to make change for `total`,
    using a greedy alortihm that uses dynamic programming.
    If change couldn't be made returns -1.
    """
    if total <= 0:
        return 0
    m = len(coins)
    coins.sort(reverse=True)
    # table[i] will be storing the minimum
    # number of coins required for i value.
    # So table[V] will have result
    table = [0 for i in range(total + 1)]

    # Base case (If given value V is 0)
    table[0] = 0

    # Initialize all table values as Infinite
    for i in range(1, total + 1):
        table[i] = sys.maxsize

    # Compute minimum coins required
    # for all values from 1 to V
    for i in range(1, total + 1):

        # Go through all coins smaller than i
        for j in range(m):
            if (coins[j] <= i):
                sub_res = table[i - coins[j]]
                if (sub_res != sys.maxsize and sub_res + 1 < table[i]):
                    table[i] = sub_res + 1

    if table[total] == sys.maxsize:
        return -1

    return table[total]
