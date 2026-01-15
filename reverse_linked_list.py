"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""

from typing import Optional
from runner import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse Linked List (LeetCode #206)

        Given the head of a singly linked list, reverse the list, and return
        the reversed list.

        Example 1:
        Input: head = [1,2,3,4,5]
        Output: [5,4,3,2,1]

        Example 2:
        Input: head = [1,2]
        Output: [2,1]

        Example 3:
        Input: head = []
        Output: []

        Constraints:
        - The number of nodes in the list is in the range [0, 5000]
        - -5000 <= Node.val <= 5000

        Follow up: Can you solve it both iteratively and recursively?
        """
        prev = None
        curr = head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev


# Helper functions for testing
def list_to_linked(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def linked_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# Test cases: list of (args_tuple, expected_output)
TEST_CASES = [
    ((list_to_linked([1, 2, 3, 4, 5]),), list_to_linked([5, 4, 3, 2, 1])),
    ((list_to_linked([1, 2]),), list_to_linked([2, 1])),
    ((list_to_linked([]),), list_to_linked([])),
    ((list_to_linked([1]),), list_to_linked([1])),
]

# Name of the method to test
METHOD_NAME = "reverseList"


# Custom test wrapper needed for linked list conversion
def run_test(solution, args, expected):
    head = list_to_linked(args[0])
    result = solution.reverseList(head)
    return linked_to_list(result) == expected
