"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List


class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        """
        Standard binary search to find target in sorted array.
        Returns index of target, or -1 if not found.

        Example: LeetCode #704 - Binary Search
        """
        if nums == []:
            return -1

        left = 0
        right = len(nums) - 1
        found = -1

        while left <= right:
            midpoint = left + ((right - left) // 2)
            located = nums[midpoint]

            if located == target:
                found = midpoint
                break

            if target > located:
                left = midpoint + 1
            elif target < located:
                right = midpoint - 1

        return found


# Test cases: list of (args_tuple, expected_output)
# Each args_tuple contains the arguments to pass to the method
TEST_CASES = [
    # Basic cases
    (([-1, 0, 3, 5, 9, 12], 9), 4),
    (([-1, 0, 3, 5, 9, 12], 2), -1),
    # Edge cases
    (([5], 5), 0),
    (([5], -5), -1),
    (([1, 2, 3], 10), -1),  # Target larger than all elements
    # Empty array - uncomment if needed
    # (([], 0), -1),
]

# Name of the method to test
METHOD_NAME = "binarySearch"
