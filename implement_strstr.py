"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Find the Index of the First Occurrence in a String (LeetCode #28)

        Given two strings needle and haystack, return the index of the first
        occurrence of needle in haystack, or -1 if needle is not part of haystack.

        Example 1:
        Input: haystack = "sadbutsad", needle = "sad"
        Output: 0
        Explanation: "sad" occurs at index 0 and 6. First occurrence is at index 0.

        Example 2:
        Input: haystack = "leetcode", needle = "leeto"
        Output: -1
        Explanation: "leeto" did not occur in "leetcode".

        Constraints:
        - 1 <= haystack.length, needle.length <= 10^4
        - haystack and needle consist of only lowercase English characters.
        """

        # don't need to search whole string
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i

        return -1


# Test cases: list of (args_tuple, expected_output)
TEST_CASES = [
    (("sadbutsad", "sad"), 0),
    (("leetcode", "leeto"), -1),
    (("hello", "ll"), 2),
    (("aaaaa", "bba"), -1),
    (("a", "a"), 0),
]

# Name of the method to test
METHOD_NAME = "strStr"
