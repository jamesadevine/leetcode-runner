"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        Product of Array Except Self (LeetCode #238)

        Given an integer array nums, return an array answer such that answer[i]
        is equal to the product of all the elements of nums except nums[i].

        The product of any prefix or suffix of nums is guaranteed to fit in a
        32-bit integer.

        You must write an algorithm that runs in O(n) time and without using
        the division operation.

        Example 1:
        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]

        Example 2:
        Input: nums = [-1,1,0,-3,3]
        Output: [0,0,9,0,0]

        Constraints:
        - 2 <= nums.length <= 10^5
        - -30 <= nums[i] <= 30
        - The product of any prefix or suffix of nums is guaranteed to fit in
          a 32-bit integer.

        Follow up: Can you solve it in O(1) extra space complexity?
        (The output array does not count as extra space for space complexity analysis.)
        """
        n = len(nums)

        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]

        suffix = [1] * n
        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]

        print(nums)
        print(suffix)
        print(prefix)
        output = [prefix[i] * suffix[i] for i in range(n)]
        print(output)

        return output


# Test cases: list of (args_tuple, expected_output)
TEST_CASES = [
    (([1, 2, 3, 4],), [24, 12, 8, 6]),
    (([-1, 1, 0, -3, 3],), [0, 0, 9, 0, 0]),
    (([2, 3],), [3, 2]),
    (([1, 1, 1, 1],), [1, 1, 1, 1]),
]

# Name of the method to test
METHOD_NAME = "productExceptSelf"
