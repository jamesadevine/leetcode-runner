"""
#739 - Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, return an array
answer such that answer[i] is the number of days you have to wait after the ith day to get
a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pass


# Test cases: list of (args_tuple, expected_output)
TEST_CASES = [
    (([73, 74, 75, 71, 69, 72, 76, 73],), [1, 1, 4, 2, 1, 1, 0, 0]),
    (([30, 40, 50, 60],), [1, 1, 1, 0]),
    (([30, 60, 90],), [1, 1, 0]),
    (([90, 80, 70, 60],), [0, 0, 0, 0]),  # Decreasing - no warmer days
    (([50],), [0]),  # Single element
    (([50, 50, 50],), [0, 0, 0]),  # All same - need strictly warmer
]

METHOD_NAME = "dailyTemperatures"
