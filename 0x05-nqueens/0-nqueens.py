#!/usr/bin/python3
"""The N queens puzzle solution
"""
from sys import argv
from typing import List, Generator


def find_safe_columns(candidate: List[int], n: int) -> List[int]:
    """Finds list of safe columns (not attacked by already placed queens)
    in a new row to be added.

    Args:
        candidate: A candidate solution. A list of column indices of
            queens ordered by row.
        n: number of queens to place in an `n` by `n` board.

    Returns:
        (List[int]): list of indices of safe columns.
    """
    # index of next row in which the safe column is searched
    current_row = len(candidate)

    unsafe_columns = set()
    for row, col in enumerate(candidate):
        unsafe_columns.add(col)     # under attack by vertical move

        # columns in the newly added row under attack by diagonal moves
        diag_left = col - (current_row - row)
        diag_right = col + (current_row - row)
        diagonals = {d for d in (diag_left, diag_right) if d in range(0, n)}
        unsafe_columns.update(diagonals)

    # find safe columns ordered by index
    safe_columns = set(range(n)).difference(unsafe_columns)
    return sorted(list(safe_columns))


def extend(candidate: List[int], n: int) -> Generator[List[int], None, None]:
    """Adds a new row and places a queen at the first available column.
    Then moves the queen to the next safe column in same row.

    Args:
        candidate: A candidate solution. A list of column indices of
            queens ordered by row.
        n: number of queens to place in an `n` by `n` board.

    Returns:
        (Generator): first generates a new candidate with a queen placed on the
        first safe column in a new row, then on subsequent calls yields a new
        candidate by moving the queen in the last row to the next safe column.
    """
    # find safe columns in the new row to be added
    next_columns = find_safe_columns(candidate, n)
    for next_column in next_columns:
        # place queen in a newly added row and move to right
        yield candidate + [next_column]


def backtrack(n: int, candidate: List[int] = []):
    """
    Using the bactrack algorithm, prints solutions to the N queens puzzle. It
    places `n` no. of queens in non-attacking positions in an `n` by `n` board.

    Args:
        candidate: A candidate solution. A list of column indices of
            queens for each row.
        n (minimum 4): number of queens to place in an `n` by `n` board.

    Note:
        A solution is a list of row and column indices for `n` number of
        queens. There may be more than one solution for given `n`.
    """
    if len(candidate) == n:     # all `n` queens placed
        print([[row, col] for row, col in enumerate(candidate)])
        return                  # can not extend solution

    # search solution in a DFS manner using recursion by
    # placing the queen on next row at first available column,
    # then move queen to next available column in same row.
    for new_candidate in extend(candidate, n):
        backtrack(n, new_candidate)


if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)

    try:
        n = int(argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    backtrack(n)
