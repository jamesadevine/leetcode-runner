"""
There is a robot on an m x n grid. The robot is initially located at the
top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right
corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right
at any point in time.

Given the two integers m and n, return the number of possible unique paths that
the robot can take to reach the bottom-right corner.


Example 1:

Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach
the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # TODO: Implement your solution here
        pass


TEST_CASES = [
    # Example 1: 3x7 grid
    ((3, 7), 28),
    # Example 2: 3x2 grid
    ((3, 2), 3),
    # 1x1 grid - only one cell, already at destination
    ((1, 1), 1),
    # Single row - only one path (all right moves)
    ((1, 5), 1),
    # Single column - only one path (all down moves)
    ((5, 1), 1),
    # 2x2 grid
    ((2, 2), 2),
    # Larger grid
    ((7, 3), 28),
]

METHOD_NAME = "uniquePaths"
