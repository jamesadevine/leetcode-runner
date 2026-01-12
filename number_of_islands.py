"""
#200 - Number of Islands

Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally
or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        x_len = len(grid[0])
        y_len = len(grid)

        # find a one, recursively sink 1 -> 0
        def sink(x: int, y: int):
            if x < 0 or x >= x_len:
                return
            if y < 0 or y >= y_len:
                return
            if grid[y][x] == "0":
                return

            grid[y][x] = "0"

            sink(x + 1, y)
            sink(x - 1, y)
            sink(x, y + 1)
            sink(x, y - 1)

        for y in range(y_len):
            for x in range(x_len):
                if grid[y][x] == "1":
                    count += 1
                    sink(x, y)

        return count


# Test cases: list of (args_tuple, expected_output)
TEST_CASES = [
    # Example 1: One large island
    (
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
        ),
        1,
    ),
    # Example 2: Three islands
    (
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
        ),
        3,
    ),
    # Single cell island
    (([["1"]],), 1),
    # No islands
    (([["0", "0"], ["0", "0"]],), 0),
]

METHOD_NAME = "numIslands"
