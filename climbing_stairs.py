"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Input: n = 4
Output: 5
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step + 1
2. 1 step + 2 steps + 1
3. 2 steps + 2 steps
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        pass


TEST_CASES = [
    # Example 1: n = 2 → 2 ways
    ((2,), 2),
    # Example 2: n = 3 → 3 ways
    ((3,), 3),
    # n = 1 → 1 way (just take 1 step)
    ((1,), 1),
    # n = 4 → 5 ways
    ((4,), 5),
]

METHOD_NAME = "climbStairs"
