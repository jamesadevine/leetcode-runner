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
        pass


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
