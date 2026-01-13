"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Trapping Rain Water (LeetCode #42)

        Given n non-negative integers representing an elevation map where
        the width of each bar is 1, compute how much water it can trap
        after raining.

        Example 1:
        Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
        Output: 6
        Explanation: The elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
        In this case, 6 units of rain water are being trapped.

        Example 2:
        Input: height = [4,2,0,3,2,5]
        Output: 9

        Constraints:
        - n == height.length
        - 1 <= n <= 2 * 10^4
        - 0 <= height[i] <= 10^5
        """

        n = len(height)

        if n == 0:
            return 0

        dp = [0] * n

        # base cases
        # we know no water can be trapped here
        dp[0] = 0
        dp[n - 1] = 0

        for i in range(1, n - 1):
            max_left = max([height[j] for j in range(i)])
            max_right = max([height[j] for j in range(i + 1, n)])

            if height[i] < max_left and height[i] < max_right:
                dp[i] = min(max_left, max_right) - height[i]

        return sum(dp)


# Test cases: list of (args_tuple, expected_output)
# Each args_tuple contains the arguments to pass to the method
TEST_CASES = [
    (([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],), 6),
    (([4, 2, 0, 3, 2, 5],), 9),
    (([],), 0),
    (([1],), 0),
    (([1, 2, 3, 4, 5],), 0),  # ascending - no water trapped
    (([5, 4, 3, 2, 1],), 0),  # descending - no water trapped
]

# Name of the method to test
METHOD_NAME = "trap"
