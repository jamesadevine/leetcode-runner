"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).



Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false

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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        pass


# Each args_tuple contains the arguments to pass to the method
TEST_CASES = [
    # Example 1: [1,2,2,3,4,4,3] - symmetric
    (
        (
            TreeNode(
                1,
                TreeNode(2, TreeNode(3), TreeNode(4)),
                TreeNode(2, TreeNode(4), TreeNode(3)),
            ),
        ),
        True,
    ),
    # Example 2: [1,2,2,null,3,null,3] - not symmetric
    (
        (TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3))),),
        False,
    ),
    # Single node - symmetric
    (
        (TreeNode(1),),
        True,
    ),
    # Two levels, symmetric: [1,2,2]
    (
        (TreeNode(1, TreeNode(2), TreeNode(2)),),
        True,
    ),
    # Two levels, not symmetric: [1,2,3]
    (
        (TreeNode(1, TreeNode(2), TreeNode(3)),),
        False,
    ),
    # Symmetric with outer children: [1,2,2,3,null,null,3]
    # Left has left child, Right has right child - this IS symmetric!
    (
        (TreeNode(1, TreeNode(2, TreeNode(3), None), TreeNode(2, None, TreeNode(3))),),
        True,
    ),
    # NOT symmetric: both subtrees have children on the same side
    # [1,2,2,3,null,3,null] - left.left=3, right.left=3 (should be right.right for symmetry)
    (
        (TreeNode(1, TreeNode(2, TreeNode(3), None), TreeNode(2, TreeNode(3), None)),),
        False,
    ),
    # NOT symmetric: both have right children
    # [1,2,2,null,3,null,3]
    (
        (TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3))),),
        False,
    ),
    # NOT symmetric: different values at mirrored positions
    (
        (TreeNode(1, TreeNode(2, TreeNode(3), None), TreeNode(2, None, TreeNode(4))),),
        False,
    ),
    # Symmetric with inner children only: [1,2,2,null,3,3,null]
    (
        (TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, TreeNode(3), None)),),
        True,
    ),
    # Deeper symmetric tree
    (
        (
            TreeNode(
                1,
                TreeNode(2, TreeNode(3, TreeNode(4), None), None),
                TreeNode(2, None, TreeNode(3, None, TreeNode(4))),
            ),
        ),
        True,
    ),
    # Same values but wrong structure at deeper level
    (
        (
            TreeNode(
                1,
                TreeNode(2, TreeNode(3, TreeNode(4), None), None),
                TreeNode(2, None, TreeNode(3, TreeNode(4), None)),
            ),
        ),
        False,
    ),
]

# Name of the method to test
METHOD_NAME = "isSymmetric"
