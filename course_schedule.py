"""
#207 - Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that
you must take course bi first if you want to take course ai.

Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are 2 courses to take. To take course 1 you should have finished course 0.
So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are 2 courses to take. To take course 1 you should have finished course 0,
and to take course 0 you should also have finished course 1. So it is impossible.

Approach: Topological Sort (detect cycle in directed graph)
Option 1: DFS - detect back edges (cycle)
Option 2: BFS (Kahn's algorithm) - process nodes with 0 in-degree

Time: O(V + E) where V = numCourses, E = len(prerequisites)
Space: O(V + E) for adjacency list
"""

from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build a map of courses and prereqs
        courses = defaultdict(list)

        for course, prereq in prerequisites:
            courses[course].append(prereq)

        # need to maintain which courses have been visited
        # 0 not visited
        # 1 visiting
        # 2 already validated
        state = [0] * numCourses

        def traverse(course) -> bool:
            # cycle!
            if state[course] == 1:
                return False

            # already processed as safe
            if state[course] == 2:
                return True

            state[course] = 1

            for prereq in courses[course]:
                if not traverse(prereq):
                    return False

            state[course] = 2

            return True

        return all(
            [
                traverse(
                    i,
                )
                for i in range(numCourses)
            ]
        )


# Test cases: list of (args_tuple, expected_output)
TEST_CASES = [
    ((2, [[1, 0]]), True),
    ((2, [[1, 0], [0, 1]]), False),
    ((1, []), True),
    ((3, [[1, 0], [2, 1]]), True),  # Linear chain
    ((3, [[1, 0], [2, 0]]), True),  # Multiple depend on one
    ((4, [[1, 0], [2, 1], [3, 2], [1, 3]]), False),  # Cycle in larger graph
]

METHOD_NAME = "canFinish"
