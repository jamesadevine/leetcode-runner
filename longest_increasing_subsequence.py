"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Longest Increasing Subsequence (LeetCode #300)

        Given an integer array nums, return the length of the longest
        strictly increasing subsequence.

        A subsequence is a sequence derived from an array by deleting some
        or no elements without changing the order of remaining elements.

        Example 1:
        Input: nums = [10,9,2,5,3,7,101,18]
        Output: 4
        Explanation: The longest increasing subsequence is [2,3,7,101]

        Example 2:
        Input: nums = [0,1,0,3,2,3]
        Output: 4

        Example 3:
        Input: nums = [7,7,7,7,7,7,7]
        Output: 1

        Constraints:
        - 1 <= nums.length <= 2500
        - -10^4 <= nums[i] <= 10^4

        Follow up: Can you come up with an algorithm that runs in O(n log n)?
        """
        # todo implement binary search approach
        pass


# Test cases: list of (args_tuple, expected_output)
# Each args_tuple contains the arguments to pass to the method
TEST_CASES = [
    (([10, 9, 2, 5, 3, 7, 101, 18],), 4),
    (([0, 1, 0, 3, 2, 3],), 4),
    (([7, 7, 7, 7, 7, 7, 7],), 1),
    (([1, 3, 6, 7, 9, 4, 10, 5, 6],), 6),
]

# Name of the method to test
METHOD_NAME = "lengthOfLIS"
