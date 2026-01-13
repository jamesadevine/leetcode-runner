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
        pass


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
