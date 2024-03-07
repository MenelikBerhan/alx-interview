#!/usr/bin/python3
"""
Perimeter of a Grid
-------------------
  where a grid is a list of list of integers:
    0 represents water
    1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    grid is rectangular, with its width and height not exceeding 100
  The grid is completely surrounded by water
  There is only one island (or nothing).
  The island doesn't have “lakes”
  (water inside that isn't connected to the water surrounding the island).

  Eg.
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
  print(island_perimeter(grid)) == 12
"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid."""
    perimeter = grid[0].count(1)
    for r in range(len(grid)):      # stop before last row (all zero)
        curr_row = grid[r]
        nxt_row = [0] * len(grid[r]) if r == len(grid) - 1 else grid[r + 1]
        # print(f'start: {perimeter}')
        # print(f'curr:{curr_row}')
        # print(f'nxxt:{nxt_row}')
        # for horizontal edges b/n current row and the one below,
        # add one to perimeter for each grid[r] + grid[r + 1] == 1
        perimeter += list(map(lambda x, y: x + y, curr_row, nxt_row)).count(1)
        # print(f'after horiz update: {perimeter}')
        # for vertical edges b/n cells in current row,
        # add one to perimeter for each grid[r][i] + grid[r][i + 1] == 1
        perimeter += list(
            map(lambda x, y: x + y, [0] + curr_row, curr_row + [0])
            ).count(1)
        # print(f'after vert update: {perimeter}')
    return perimeter


""" # map overkill
def island_perimeter(grid: 'list[list[int]]') -> int:
    def map_function(curr_row, nxt_row):s
        perimeter = 0
        # for horizontal edges b/n current row and the one below,
        # add one to perimeter for each grid[r] + grid[r + 1] == 1
        perimeter += list(map(lambda x, y: x + y, curr_row, nxt_row)).count(1)

        # for vertical edges b/n cells in current row,
        # add one to perimeter for each grid[r][i] + grid[r][i + 1] == 1
    perimeter += list(map(lambda x, y: x + y, curr_row, curr_row[1:])).count(1)

        return perimeter

    return sum(map(map_function, grid[:-1], grid[1:])) """
