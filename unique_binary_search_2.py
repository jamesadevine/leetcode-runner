"""
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.



Example 1:


Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:

Input: n = 1
Output: [[1]]

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
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        pass


# Each args_tuple contains the arguments to pass to the method
TEST_CASES = [
    (
        (3,),
        [
            TreeNode(1, None, TreeNode(2, None, TreeNode(3))),
            TreeNode(1, None, TreeNode(3, TreeNode(2), None)),
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(3, TreeNode(1, None, TreeNode(2)), None),
            TreeNode(3, TreeNode(2, TreeNode(1), None), None),
        ],
    ),
    (
        (1,),
        [TreeNode(1)],
    ),
]

# Name of the method to test
METHOD_NAME = "generateTrees"
