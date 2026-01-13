"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Sort an Array (LeetCode #912)

        Given an array of integers nums, sort the array in ascending order
        and return it.

        You must solve the problem without using any built-in functions in
        O(nlog(n)) time complexity and with the smallest space complexity possible.

        Example 1:
        Input: nums = [5,2,3,1]
        Output: [1,2,3,5]
        Explanation: After sorting the array, the positions become [1,2,3,5].

        Example 2:
        Input: nums = [5,1,1,2,0,0]
        Output: [0,0,1,1,2,5]
        Explanation: Note that values can be duplicated.

        Constraints:
        - 1 <= nums.length <= 5 * 10^4
        - -5 * 10^4 <= nums[i] <= 5 * 10^4

        Approaches:
        1. Merge Sort - O(n log n) time, O(n) space, stable
        2. Quick Sort - O(n log n) avg, O(n²) worst, O(log n) space
        3. Heap Sort - O(n log n) time, O(1) space
        """
        pass


# Test cases: list of (args_tuple, expected_output)
TEST_CASES = [
    (([5, 2, 3, 1],), [1, 2, 3, 5]),
    (([5, 1, 1, 2, 0, 0],), [0, 0, 1, 1, 2, 5]),
    (([1],), [1]),
    (([2, 1],), [1, 2]),
]

# Name of the method to test
METHOD_NAME = "sortArray"
