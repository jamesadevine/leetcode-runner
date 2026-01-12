"""
#15 - 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:
Input: nums = [0,1,1]
Output: []

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]

Approach: Sort + Two Pointers
- Sort the array first
- Fix one element, then use two pointers to find pairs that sum to -fixed
- Skip duplicates to avoid duplicate triplets

Time: O(n²)
Space: O(1) excluding output (or O(n) for sorting)
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        results = []

        # sort input array
        nums = sorted(nums)

        for fixed in range(0, len(nums)):
            if fixed > 0 and nums[fixed] == nums[fixed - 1]:
                continue

            left, right = fixed + 1, len(nums) - 1
            target = -nums[fixed]

            while left < right:
                ptr_sum = nums[left] + nums[right]

                if ptr_sum == target:
                    results.append([nums[fixed], nums[left], nums[right]])
                    # Move both pointers inward, skipping duplicates
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif ptr_sum < target:
                    # result too small, increase left value
                    left += 1
                elif ptr_sum > target:
                    # result too big, decrease right value
                    right -= 1

        return results


# Test cases: list of (args_tuple, expected_output)
TEST_CASES = [
    (([-1, 0, 1, 2, -1, -4],), [[-1, -1, 2], [-1, 0, 1]]),
    (([0, 1, 1],), []),
    (([0, 0, 0],), [[0, 0, 0]]),
    (([0, 0, 0, 0],), [[0, 0, 0]]),
    (([-2, 0, 1, 1, 2],), [[-2, 0, 2], [-2, 1, 1]]),
]

METHOD_NAME = "threeSum"
