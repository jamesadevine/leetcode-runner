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

Approach: DFS/BFS
- Iterate through grid, when you find a '1', increment count and "sink" the entire island
- Use DFS or BFS to mark all connected land as visited (change to '0' or use visited set)

Time: O(m * n)
Space: O(m * n) worst case for DFS stack / BFS queue
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # TODO: Implement your solution
        # Hint: For each unvisited '1', do DFS/BFS to mark entire island
        pass


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
