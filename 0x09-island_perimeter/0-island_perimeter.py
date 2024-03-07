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
    perimeter = grid[0].count(1)    # top horizontal edges of cells in 1st row
    for r in range(len(grid)):
        curr_row = grid[r]
        # set list of zeros as nxt_row for last row
        nxt_row = grid[r + 1] if r < len(grid) - 1 else [0] * len(grid[r])

        # for horizontal edges b/n current row and the one below,
        # add one to perimeter for each grid[r] + grid[r + 1] == 1
        perimeter += list(map(lambda x, y: x + y, curr_row, nxt_row)).count(1)

        # for vertical edges b/n cells in current row,
        # add one to perimeter for each grid[r][i] + grid[r][i + 1] == 1
        perimeter += list(
            map(lambda x, y: x + y, [0] + curr_row, curr_row + [0])
            ).count(1)        # add with zero for 1st & last cell in curr_row

        # to exit loop if edge of island is reached
        if perimeter and nxt_row.count(1) == 0:
            break
    return perimeter


""" # map overkill
def island_perimeter(grid):
    # Returns the perimeter of the island described in grid.
    def map_function(curr_row, nxt_row):
        # Returns total length of horizontal edges b/n current & nxt row,
        # and vertical edges b/n each cell in current row.
        perimeter = 0
        # for horizontal edges b/n current row and the one below,
        # add one to perimeter for each grid[r] + grid[r + 1] == 1
        perimeter += list(map(lambda x, y: x + y, curr_row, nxt_row)).count(1)

        # for vertical edges b/n cells in current row,
        # add one to perimeter for each grid[r][i] + grid[r][i + 1] == 1.
        # (add with zero for 1st & last cell in curr_row)
        perimeter += list(
            map(lambda x, y: x + y, [0] + curr_row, curr_row + [0])
        ).count(1)

        return perimeter

    # sum edges found b/n rows and b/n cells in rows
    return sum(
        map(
            map_function,
            [[0] * len(grid[0])] + grid,    # add row of zeros before 1st row &
            grid + [[0] * len(grid[0])]     # after last row, for horizontal
        )                                   # edges in 1st & last row
    )
 """
