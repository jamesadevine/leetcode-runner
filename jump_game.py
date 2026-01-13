"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Jump Game (LeetCode #55)

        You are given an integer array nums. You are initially positioned
        at the array's first index, and each element in the array represents
        your maximum jump length at that position.

        Return true if you can reach the last index, or false otherwise.

        Example 1:
        Input: nums = [2,3,1,1,4]
        Output: true
        Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

        Example 2:
        Input: nums = [3,2,1,0,4]
        Output: false
        Explanation: You will always arrive at index 3 no matter what.
        Its maximum jump length is 0, which makes it impossible to reach the last index.

        Constraints:
        - 1 <= nums.length <= 10^4
        - 0 <= nums[i] <= 10^5

        Approach: Greedy
        - Track the furthest index we can reach
        - For each index i (if reachable), update furthest = max(furthest, i + nums[i])
        - If furthest >= last index, return True
        - If we're stuck (i > furthest), return False
        """
        pass


# Test cases: list of (args_tuple, expected_output)
TEST_CASES = [
    (([2, 3, 1, 1, 4],), True),
    (([3, 2, 1, 0, 4],), False),
    (([0],), True),
    (([2, 0, 0],), True),
    (([1, 0, 1, 0],), False),
]

# Name of the method to test
METHOD_NAME = "canJump"
