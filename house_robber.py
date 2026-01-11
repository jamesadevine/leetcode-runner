"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # this is not left right, it is dp
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(dp)):
            # we either take the previous node value (noop) or we become the higher value, taking the our value plus the value two houses back
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return max(dp)


TEST_CASES = [
    # Example 1: nums = [1,2,3,1] → 4 (rob house 0 and 2)
    (([1, 2, 3, 1],), 4),
    # Example 2: nums = [2,7,9,3,1] → 12 (rob house 0, 2, and 4)
    (([2, 7, 9, 3, 1],), 12),
]

METHOD_NAME = "rob"
