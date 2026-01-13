"""
#21 - Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together
the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
- The number of nodes in both lists is in the range [0, 50]
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order

Approach: Two Pointers / Iterative
- Use a dummy head to simplify edge cases
- Compare current nodes from both lists
- Attach the smaller one to result, advance that pointer
- O(m + n) time, O(1) space
"""

from typing import Optional
from runner import ListNode


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # the first value of each list is the lowest, the lower of the two will be the head

        dummy = ListNode()
        writer = dummy
        p1 = list1
        p2 = list2

        while p1 and p2:
            if p1.val < p2.val:
                tmp = p1.next
                p1.next = None
                writer.next = p1
                p1 = tmp
            else:
                tmp = p2.next
                p2.next = None
                writer.next = p2
                p2 = tmp
            writer = writer.next
        if p1:
            writer.next = p1
        if p2:
            writer.next = p2

        return dummy.next


# Test cases: list of (args_tuple, expected_output)
TEST_CASES = [
    (([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4]),
    (([], []), []),
    (([], [0]), [0]),
    (([5], [1, 2, 4]), [1, 2, 4, 5]),
    (([1, 3, 5, 7], [2, 4, 6, 8]), [1, 2, 3, 4, 5, 6, 7, 8]),
]

METHOD_NAME = "mergeTwoLists"

# Custom test runner for linked list problems
LINKED_LIST_ARGS = True  # Signals that args need conversion
