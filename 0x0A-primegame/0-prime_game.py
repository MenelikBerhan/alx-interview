#!/usr/bin/python3
"""Prime Game puzzle solution
"""


def isWinner(x: int, nums: 'list[int]') -> str:
    """Based on the above description of the Prime Game, determines the winner.

    Args:
    x (int): no. of rounds (length of `nums`)
    nums (list[int]): `n` for each round.

    Returns:
    (str | None): name of the player that won the most rounds, or
        None if the winner cannot be determined.
    """

    def find_prime(n: int) -> 'list[int]':
        """Finds list of prime no.s less than or equal to `n`
        using the sieve of Eratosthenes algorithm."""
        if n <= 1:
            return []
        # initialize a list of boolean values indexed by integers 2 to n.
        # value in list indicates if index integer is prime or not
        is_prime_list = [True for i in range(n + 1)]
        # set values at index 0 & 1 to false since 0 & 1 are not prime no.s
        is_prime_list[0] = False
        is_prime_list[1] = False

        # for i = 2, 3, 4, ..., not exceeding √n
        for i in range(int(n**0.5 + 1)):
            if is_prime_list[i]:    # i is a prime no.
                # set indexs at multiples of i to False (not prime) starting
                #   from i^2 since we've already set all smaller multiples of
                #   i to False in previous loops
                for j in range(i**2, n + 1, i):
                    is_prime_list[j] = False

        # retrun indices where is_prime_list[index] is True (prime no.)
        return [i for i in range(n + 1) if is_prime_list[i]]
    if x < 1:
        return None

    # Since at every turn each player selects a prime no. & its multiples,
    #   there are len(list of prime no.s less than n) moves available before
    #   only number 1 remains. Therefore if primes list length is even,
    #   the player who goes second win, else the player who goes first win.
    # For each round maria always goes first.
    rounds_won_by_ben = rounds_won_by_maria = 0
    for n in nums:
        primes_list = find_prime(n)
        if (len(primes_list) % 2 == 0):  # primes list length is even, Ben wins
            rounds_won_by_ben += 1
        else:
            rounds_won_by_maria += 1  # primes list length is odd, Maria wins

    if rounds_won_by_maria > rounds_won_by_ben:
        return 'Maria'
    elif rounds_won_by_maria < rounds_won_by_ben:
        return 'Ben'
    return None     # equal rounds won
