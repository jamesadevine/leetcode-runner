from typing import Optional, List

"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.



Example 1:

Input: root = [1,null,2,3]

Output: [1,3,2]

Explanation:



Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,2,6,5,7,1,3,9,8]

Explanation:



Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]
"""


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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        pass


# Each args_tuple contains the arguments to pass to the method
TEST_CASES = [
    # Example 1: [1,null,2,3] -> [1,3,2]
    (
        (TreeNode(1, None, TreeNode(2, TreeNode(3), None)),),
        [1, 3, 2],
    ),
    # Example 2: [1,2,3,4,5,null,8,null,null,6,7,9] -> [4,2,6,5,7,1,3,9,8]
    (
        (
            TreeNode(
                1,
                TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))),
                TreeNode(3, None, TreeNode(8, TreeNode(9), None)),
            ),
        ),
        [4, 2, 6, 5, 7, 1, 3, 9, 8],
    ),
    # Example 3: [] -> []
    (
        (None,),
        [],
    ),
    # Example 4: [1] -> [1]
    (
        (TreeNode(1),),
        [1],
    ),
]

# Name of the method to test
METHOD_NAME = "inorderTraversal"
