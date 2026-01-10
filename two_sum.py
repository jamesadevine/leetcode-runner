"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""

from typing import List


class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         num1 = nums[i]
    #         for j in range(i + 1, len(nums)):
    #             num2 = nums[j]
    #             if target == num1 + num2:
    #                 return [i, j]
    #     return []

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Example: Two Sum (LeetCode #1)
        Given an array of integers nums and an integer target,
        return indices of the two numbers such that they add up to target.
        """
        seen = {}

        for idx, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], idx]

            seen[num] = idx
        return []

    #


# Test cases: list of (args_tuple, expected_output)
# Each args_tuple contains the arguments to pass to the method
TEST_CASES = [
    (([2, 7, 11, 15], 9), [0, 1]),
    (([3, 2, 4], 6), [1, 2]),
    (([3, 3], 6), [0, 1]),
]

# Name of the method to test
METHOD_NAME = "twoSum"
