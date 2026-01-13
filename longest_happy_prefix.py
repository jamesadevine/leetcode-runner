"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""


class Solution:
    def longestPrefix(self, s: str) -> str:
        """
        Longest Happy Prefix (LeetCode #1392)

        A string is called a happy prefix if is a non-empty prefix which is
        also a suffix (excluding itself).

        Given a string s, return the longest happy prefix of s. Return an
        empty string "" if no such prefix exists.

        Example 1:
        Input: s = "level"
        Output: "l"
        Explanation: s contains 4 prefixes excluding itself ("l", "le", "lev", "leve"),
        and suffix ("l", "el", "vel", "evel"). The largest prefix which is also
        suffix is "l".

        Example 2:
        Input: s = "ababab"
        Output: "abab"
        Explanation: "abab" is the largest prefix which is also suffix.
        They can overlap in the original string.

        Constraints:
        - 1 <= s.length <= 10^5
        - s contains only lowercase English letters.

        Approaches:
        1. KMP Failure Function: Build the failure/LPS array, answer is s[:lps[-1]]
        2. Z-Algorithm: Find Z[i] where Z[i] + i == n
        3. Rolling Hash: Compare prefix and suffix hashes
        """
        pass


# Test cases: list of (args_tuple, expected_output)
TEST_CASES = [
    (("level",), "l"),
    (("ababab",), "abab"),
    (("leetcodeleet",), "leet"),
    (("a",), ""),
    (("abcabc",), "abc"),
]

# Name of the method to test
METHOD_NAME = "longestPrefix"
