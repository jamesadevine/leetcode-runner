"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val}"

    def __eq__(self, value):
        return self.val == value


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        pass


# Each args_tuple contains the arguments to pass to the method
TEST_CASES = [
    # Even length: [1,2,3,4] -> [1,4,2,3]
    (
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4))))),
        (ListNode(1, ListNode(4, ListNode(2, ListNode(3))))),
    ),
    # Odd length: [1,2,3,4,5] -> [1,5,2,4,3]
    (
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))),
        (ListNode(1, ListNode(5, ListNode(2, ListNode(4, ListNode(3)))))),
    ),
    # Two elements: [1,2] -> [1,2]
    (
        (ListNode(1, ListNode(2))),
        (ListNode(1, ListNode(2))),
    ),
    # Single element: [1] -> [1]
    (
        (ListNode(1)),
        (ListNode(1)),
    ),
    # Three elements: [1,2,3] -> [1,3,2]
    (
        (ListNode(1, ListNode(2, ListNode(3)))),
        (ListNode(1, ListNode(3, ListNode(2)))),
    ),
]

# Name of the method to test
METHOD_NAME = "reorderList"
