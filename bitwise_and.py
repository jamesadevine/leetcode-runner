"""
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.



Example 1:

Input: left = 5, right = 7
Output: 4
Example 2:

Input: left = 0, right = 0
Output: 0
Example 3:

Input: left = 1, right = 2147483647
Output: 0


Constraints:

0 <= left <= right <= 231 - 1
"""


class Solution:
    def bitwiseAnd(self, left: int, right: int) -> int:
        pass


# Each args_tuple contains the arguments to pass to the method
TEST_CASES = [
    (
        (5, 7),
        (4),
    ),
    (
        (0, 0),
        (0),
    ),
    (
        (1, 2147483647),
        (0),
    ),
]

# Name of the method to test
METHOD_NAME = "bitwiseAnd"
