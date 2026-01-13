"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.



Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"[{self.val}]"

    def __eq__(self, value):
        return self.val == value


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        pass


# Each args_tuple contains the arguments to pass to the method
TEST_CASES = [
    # Example 1: [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    # Path: 5 -> 4 -> 11 -> 2 = 22
    (
        (
            TreeNode(
                5,
                TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None),
                TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))),
            ),
            22,
        ),
        True,
    ),
    # Example 2: [1,2,3], targetSum = 5
    # Paths: 1->2=3, 1->3=4, neither equals 5
    (
        (TreeNode(1, TreeNode(2), TreeNode(3)), 5),
        False,
    ),
    # Example 3: [], targetSum = 0
    # Empty tree has no root-to-leaf paths
    (
        (None, 0),
        False,
    ),
    # BUG TEST 1: Non-leaf path - targetSum equals root value but root is not a leaf
    # Tree: [1, 2, null] - only path is 1->2=3, not 1
    # Should return False (no leaf path sums to 1)
    (
        (TreeNode(1, TreeNode(2), None), 1),
        False,
    ),
    # BUG TEST 2: Non-leaf path on right side
    # Tree: [1, null, 2] - only path is 1->2=3
    # Should return False (no leaf path sums to 1)
    (
        (TreeNode(1, None, TreeNode(2)), 1),
        False,
    ),
    # BUG TEST 3: Negative values - path temporarily exceeds target
    # Tree: [10, 5, -3] - paths: 10->5=15, 10->-3=7
    # targetSum = 7, should return True via the negative path
    (
        (TreeNode(10, TreeNode(5), TreeNode(-3)), 7),
        True,
    ),
    # BUG TEST 4: Negative values causing sum to go above then below target
    # Tree: [1, 2, -1, null, null, 3, null]
    # Paths: 1->2=3, 1->-1->3=3
    # targetSum = 3
    (
        (TreeNode(1, TreeNode(2), TreeNode(-1, TreeNode(3), None)), 3),
        True,
    ),
    # Single node equals target - this IS a leaf
    (
        (TreeNode(5), 5),
        True,
    ),
    # Single node does not equal target
    (
        (TreeNode(5), 3),
        False,
    ),
]

# Name of the method to test
METHOD_NAME = "hasPathSum"
