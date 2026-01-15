"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Search in Rotated Sorted Array (LeetCode #33)

        There is an integer array nums sorted in ascending order (with distinct values).

        Prior to being passed to your function, nums is possibly rotated at an
        unknown pivot index k (1 <= k < nums.length) such that the resulting
        array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]].

        For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and
        become [4,5,6,7,0,1,2].

        Given the array nums after the possible rotation and an integer target,
        return the index of target if it is in nums, or -1 if it is not in nums.

        You must write an algorithm with O(log n) runtime complexity.

        Example 1:
        Input: nums = [4,5,6,7,0,1,2], target = 0
        Output: 4

        Example 2:
        Input: nums = [4,5,6,7,0,1,2], target = 3
        Output: -1

        Example 3:
        Input: nums = [1], target = 0
        Output: -1

        Constraints:
        - 1 <= nums.length <= 5000
        - -10^4 <= nums[i] <= 10^4
        - All values of nums are unique.
        - nums is an ascending array that is possibly rotated.
        - -10^4 <= target <= 10^4
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            if nums[left] <= nums[middle]:
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1

        return -1


# Test cases: list of (args_tuple, expected_output)
TEST_CASES = [
    (([4, 5, 6, 7, 0, 1, 2], 0), 4),
    (([4, 5, 6, 7, 0, 1, 2], 3), -1),
    (([1], 0), -1),
    (([1], 1), 0),
    (([3, 1], 1), 1),
    (([5, 1, 3], 3), 2),
    (([3, 4, 5, 1, 2], 1), 3),  # target is in the "unsorted" half
]

# Name of the method to test
METHOD_NAME = "search"
