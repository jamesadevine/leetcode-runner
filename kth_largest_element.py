"""
#215 - Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Approaches:
1. Sort: O(n log n) time, O(1) space
2. Min Heap of size k: O(n log k) time, O(k) space
3. Quick Select: O(n) average, O(n²) worst time, O(1) space

Time: O(n log k) with heap, O(n) average with quick select
Space: O(k) with heap, O(1) with quick select
"""

from typing import List
import heapq


"""
heap solution
heap = []

for num in nums:
    heapq.heappush(heap, num)
    if len(heap) > k:
        heapq.heappop(heap)

return heap[0]
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Quick Select approach - O(n) average time, O(1) space"""
        target = len(nums) - k  # Index where kth largest would be if sorted

        def partition(left: int, right: int) -> int:
            """Lomuto partition: pivot is last element"""
            pivot = nums[right]
            store = left

            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store], nums[i] = nums[i], nums[store]
                    store += 1

            # Put pivot in its final position
            nums[store], nums[right] = nums[right], nums[store]
            return store

        def quick_select(left: int, right: int) -> int:
            if left == right:
                return nums[left]

            pivot_idx = partition(left, right)

            if pivot_idx == target:
                return nums[pivot_idx]
            elif pivot_idx < target:
                return quick_select(pivot_idx + 1, right)  # Go right
            else:
                return quick_select(left, pivot_idx - 1)  # Go left

        return quick_select(0, len(nums) - 1)


# Test cases: list of (args_tuple, expected_output)
TEST_CASES = [
    (([3, 2, 1, 5, 6, 4], 2), 5),
    (([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4),
    (([1], 1), 1),
    (([2, 1], 1), 2),
    (([2, 1], 2), 1),
    (([-1, -2, -3, -4], 2), -2),
]

METHOD_NAME = "findKthLargest"
