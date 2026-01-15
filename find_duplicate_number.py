"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        """
        Find the Duplicate Number (LeetCode #287)

        Given an array of integers nums containing n + 1 integers where each
        integer is in the range [1, n] inclusive.

        There is only one repeated number in nums, return this repeated number.

        You must solve the problem without modifying the array nums and using
        only constant extra space.

        Example 1:
        Input: nums = [1,3,4,2,2]
        Output: 2

        Example 2:
        Input: nums = [3,1,3,4,2]
        Output: 3

        Example 3:
        Input: nums = [3,3,3,3,3]
        Output: 3

        Constraints:
        - 1 <= n <= 10^5
        - nums.length == n + 1
        - 1 <= nums[i] <= n
        - All the integers in nums appear only once except for precisely one
          integer which appears two or more times.
        """
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            # find where the lists interesect
            if slow == fast:
                break

        slow2 = 0

        # number of nodes before cycle == the number of nodes of the cycle
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow


METHOD_NAME = "findDuplicate"

# Test cases: list of (args_tuple, expected_output)
TEST_CASES = [
    (([1, 3, 4, 2, 2],), 2),
    (([3, 1, 3, 4, 2],), 3),
    (([3, 3, 3, 3, 3],), 3),
    (([1, 1],), 1),
    (([2, 2, 2, 2, 2],), 2),
]
