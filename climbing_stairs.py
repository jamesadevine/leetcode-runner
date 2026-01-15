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
        # relationship is the previous max (dp value - 1, dp value - 2) + 1

        # ensure no oob access
        if n == 1:
            return 1

        if n == 2:
            return 2

        dp = [0] * n

        # the first step is always 1
        # (only 1 way to climb the first step)
        dp[0] = 1
        # the second step is either the two single steps or 1 double step
        dp[1] = 2

        for i in range(2, n):
            print(dp[i - 1], dp[i - 2])
            dp[i] = dp[i - 1] + dp[i - 2]  # sum the previous two distinct ways

        return dp[n - 1]


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
