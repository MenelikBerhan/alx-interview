#!/usr/bin/python3
"""Prime Game Puzzle Solution
Maria and Ben are playing a game. Given a set of consecutive integers starting
from `1` up to and including `n`, they take turns choosing a prime number from
the set and removing that number and its multiples from the set. The player
that cannot make a move loses the game.

They play `x` rounds of the game, where `n` may be different for each round.
Assuming Maria always goes first and both players play optimally,
determine who the winner of each game is.
"""

"""Sieve of Eratosthenes algorithm for finding list of prime no.s <= n
    input: an integer n > 1.
    output: all prime numbers from 2 through n.

    let A be an array of Boolean values, indexed by integers 2 to n,
    initially all set to true.
    
    for i = 2, 3, 4, ..., not exceeding √n do
        if A[i] is true
            for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n do
                set A[j] := false

    return all i such that A[i] is true.
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
      # set indexs at multiples of i to False(not prime) starting from i^2
      #  since we've already set all the smaller multiples of i already
      for j in range(i**2, n + 1, i): 
        is_prime_list[j] = False

  # retrun indices where is_prime_list[index] is True (prime no.)
  return [i for i in range(n + 1) if is_prime_list[i]]

def isWinner(x: int, nums: 'list[int]') -> str:
  """Based on the above description of the Prime Game, determines the winner.

  Args:
    x (int): no. of rounds (length of `nums`)
    nums (list[int]): `n` for each round.
  
  Returns:
    (str | None): name of the player that won the most rounds, or
      None if the winner cannot be determined.
  """
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
    print(f'for n = {n}, primes: {primes_list}')
    if (len(primes_list) % 2 == 0): # primes list length is even, Ben wins
      rounds_won_by_ben += 1
    else:
      rounds_won_by_maria += 1  # primes list length is odd, Maria wins

  if rounds_won_by_maria > rounds_won_by_ben:
    return 'Maria'
  elif rounds_won_by_maria < rounds_won_by_ben:
    return 'Ben'
  return None     # equal rounds won
