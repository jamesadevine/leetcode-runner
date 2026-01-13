"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        pass


# Each args_tuple contains the arguments to pass to the method
TEST_CASES = [
    (
        ([3, 2, 3]),
        (3),
    ),
    (
        ([2, 2, 1, 1, 1, 2, 2]),
        (2),
    ),
]

# Name of the method to test
METHOD_NAME = "majorityElement"
