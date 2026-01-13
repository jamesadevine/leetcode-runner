"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merge k Sorted Lists (LeetCode #23)

        You are given an array of k linked-lists lists, each linked-list is
        sorted in ascending order.

        Merge all the linked-lists into one sorted linked-list and return it.

        Example 1:
        Input: lists = [[1,4,5],[1,3,4],[2,6]]
        Output: [1,1,2,3,4,4,5,6]
        Explanation: The linked-lists are:
        [1->4->5, 1->3->4, 2->6]
        merging them into one sorted list: 1->1->2->3->4->4->5->6

        Example 2:
        Input: lists = []
        Output: []

        Example 3:
        Input: lists = [[]]
        Output: []

        Constraints:
        - k == lists.length
        - 0 <= k <= 10^4
        - 0 <= lists[i].length <= 500
        - -10^4 <= lists[i][j] <= 10^4
        - lists[i] is sorted in ascending order.
        - The sum of lists[i].length will not exceed 10^4.

        Approaches:
        1. Min Heap: Push all list heads, pop min, push its next. O(N log k)
        2. Divide and Conquer: Recursively merge pairs. O(N log k)
        3. Merge one by one: O(Nk) - not optimal
        """
        pass


# Test cases require linked list construction - manual testing recommended
TEST_CASES = []
METHOD_NAME = "mergeKLists"

# Manual test helper:
# def make_list(arr):
#     dummy = ListNode()
#     curr = dummy
#     for val in arr:
#         curr.next = ListNode(val)
#         curr = curr.next
#     return dummy.next
#
# lists = [make_list([1,4,5]), make_list([1,3,4]), make_list([2,6])]
# result = Solution().mergeKLists(lists)
