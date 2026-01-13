"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.



Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        pass


# Each args_tuple contains the arguments to pass to the method
TEST_CASES = [
    # Example 1: "aab"
    (("aab",), [["a", "a", "b"], ["aa", "b"]]),
    # Example 2: single character
    (("a",), [["a"]]),
    # All same characters - multiple palindrome options
    (("aaa",), [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]),
    # No palindromes longer than 1
    (("abc",), [["a", "b", "c"]]),
    # Longer palindrome in middle
    (("aba",), [["a", "b", "a"], ["aba"]]),
    # Two characters same
    (("bb",), [["b", "b"], ["bb"]]),
    # Two characters different
    (("ab",), [["a", "b"]]),
    # Palindrome at start and end
    (("abba",), [["a", "b", "b", "a"], ["a", "bb", "a"], ["abba"]]),
    # Mixed with longer palindromes
    (
        ("aabb",),
        [["a", "a", "b", "b"], ["a", "a", "bb"], ["aa", "b", "b"], ["aa", "bb"]],
    ),
]

# Name of the method to test
METHOD_NAME = "partition"
