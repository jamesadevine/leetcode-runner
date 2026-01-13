"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Gas Station (LeetCode #134)

        There are n gas stations along a circular route, where the amount
        of gas at the ith station is gas[i].

        You have a car with an unlimited gas tank and it costs cost[i] of
        gas to travel from the ith station to its next (i + 1)th station.
        You begin the journey with an empty tank at one of the gas stations.

        Given two integer arrays gas and cost, return the starting gas
        station's index if you can travel around the circuit once in the
        clockwise direction, otherwise return -1. If there exists a solution,
        it is guaranteed to be unique.

        Example 1:
        Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
        Output: 3
        Explanation:
        Start at station 3 (index 3) and fill up with 4 unit of gas. Tank = 4
        Travel to station 4. Tank = 4 - 1 + 5 = 8
        Travel to station 0. Tank = 8 - 2 + 1 = 7
        Travel to station 1. Tank = 7 - 3 + 2 = 6
        Travel to station 2. Tank = 6 - 4 + 3 = 5
        Travel to station 3. The cost is 5. Your gas is just enough to travel back.

        Example 2:
        Input: gas = [2,3,4], cost = [3,4,3]
        Output: -1

        Constraints:
        - n == gas.length == cost.length
        - 1 <= n <= 10^5
        - 0 <= gas[i], cost[i] <= 10^4

        Approach: Greedy
        - If total gas < total cost, impossible (return -1)
        - Otherwise, solution exists. Find start point:
        - Track current tank. If it goes negative, reset start to next station
        - Key insight: if we can't reach station j from i, we also can't reach
          j from any station between i and j
        """
        pass


# Test cases: list of (args_tuple, expected_output)
TEST_CASES = [
    (([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3),
    (([2, 3, 4], [3, 4, 3]), -1),
    (([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]), 4),
]

# Name of the method to test
METHOD_NAME = "canCompleteCircuit"
