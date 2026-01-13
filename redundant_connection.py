"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Redundant Connection (LeetCode #684)

        In this problem, a tree is an undirected graph that is connected
        and has no cycles.

        You are given a graph that started as a tree with n nodes labeled
        from 1 to n, with one additional edge added. The added edge has two
        different vertices chosen from 1 to n, and was not an edge that
        already existed.

        Return an edge that can be removed so that the resulting graph is
        a tree of n nodes. If there are multiple answers, return the answer
        that occurs last in the input.

        Example 1:
        Input: edges = [[1,2],[1,3],[2,3]]
        Output: [2,3]

        Example 2:
        Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
        Output: [1,4]

        Constraints:
        - n == edges.length
        - 3 <= n <= 1000
        - edges[i].length == 2
        - 1 <= ai < bi <= edges.length
        - ai != bi
        - There are no repeated edges.
        - The given graph is connected.

        Approach: Union Find
        - Process edges one by one
        - If two nodes are already in the same set, this edge creates a cycle
        - Return the first edge that connects two already-connected nodes
        """
        pass


# Test cases: list of (args_tuple, expected_output)
TEST_CASES = [
    (([[1, 2], [1, 3], [2, 3]],), [2, 3]),
    (([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]],), [1, 4]),
]

# Name of the method to test
METHOD_NAME = "findRedundantConnection"
