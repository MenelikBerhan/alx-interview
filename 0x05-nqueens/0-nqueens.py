#!/usr/bin/python3
"""The N queens puzzle solution
"""
from sys import argv
from typing import List, Union


def find_safe_column(candidate: List[int], n: int, new_row: bool = False)\
        -> Union[int, None]:
    """Finds the first safe column (not attacked by already placed queens)
    in last row or in a new row to be added.

    Args:
        candidate: A candidate solution. A list of column indices of
            queens ordered by row.
        n: number of queens to place in an `n` by `n` board.
        new_row: if True find safe column in new row for adding new queen,
            else find safe column in last row to move last queen to right.

    Returns:
        (int | None): the index of the safe column, else None.
    """
    # index of row in which the safe column is searched
    current_row = len(candidate) if new_row else len(candidate) - 1

    unsafe_columns = set()
    for row, col in enumerate(candidate):
        # skip last row if queen is to be moved with in last row
        if row == current_row:
            continue
        unsafe_columns.add(col)     # under attack by vertical move

        # columns in `current_row` under attack by diagonal moves
        diag_left = col - (current_row - row)
        diag_right = col + (current_row - row)
        diagonals = {d for d in (diag_left, diag_right) if d in range(0, n)}
        unsafe_columns.update(diagonals)

    # start of safe column search index. Start from 0 for placing queen in
    # new row, and for moving queen, search after column of queen in last row
    start_col = candidate[-1] + 1 if not new_row else 0

    # find first column (moving left to right) not in `unsafe_columns`
    safe_columns = set(range(start_col, n)).difference(unsafe_columns)
    if safe_columns:
        return safe_columns.pop()
    return None


def first(candidate: List[int], n: int) -> Union[List[int], None]:
    """Adds a new row and places a queen at the first available column.

    Args:
        candidate: A candidate solution. A list of column indices of
            queens ordered by row.
        n: number of queens to place in an `n` by `n` board.

    Returns:
        (List[int] | None): a new candidate with added row if a queen
            can be placed in a new row, else None.
    """
    # find next safe column in new next row and if any, place new queen there
    next_column = find_safe_column(candidate, n, new_row=True)
    if next_column is None:
        return None

    # place queen in a new added row
    return candidate + [next_column]


def next(candidate: List[int], n: int) -> Union[List[int], None]:
    """Moves queen in the last row to the next available column in the same row

    Args:
        candidate: A candidate solution. A list of column indices of
            queens for each row.
        n: number of queens to place in an `n` by `n` board.

    Returns:
        (List[int] | None): returns a new candidate if the queen in last
        row can be moved to next valid column in same row, else None.
    """
    # find next safe column in last row
    next_column = find_safe_column(candidate, n)
    if next_column is None:
        return None

    # move queen in last row to new safe column in same row
    return candidate[:-1] + [next_column]


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
    if len(candidate) == n:  # all `n` queens placed
        print([[row, col] for row, col in enumerate(candidate)])
        return              # can not extend solution

    # place queen on next row at first available column
    candidate = first(candidate, n)
    while candidate is not None:
        # search solution in a DFS manner using recursion
        backtrack(n, candidate)
        # move queen on last row to next available column in same row
        candidate = next(candidate, n)


if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    n = argv[1]
    try:
        n = int(n)
    except Exception:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    backtrack(n)
