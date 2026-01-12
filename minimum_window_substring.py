"""
#76 - Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window
substring of s such that every character in t (including duplicates) is included in
the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

"""

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # Count characters needed from t
        need = Counter(t)
        required = len(need)  # Number of unique chars we need
        formed = 0  # Number of unique chars with desired frequency

        # Window pointers and answer tracking
        left = 0
        result = ""
        result_len = float("inf")

        for right in range(len(s)):
            # Expand: add s[right] to window
            char = s[right]
            if char in need:
                need[char] -= 1
                if need[char] == 0:  # Just satisfied this character
                    formed += 1

            # Shrink: while window is valid, try to minimize
            while formed == required:
                # Record this valid window if it's smaller
                window_len = right - left + 1
                if window_len < result_len:
                    result_len = window_len
                    result = s[left : right + 1]

                # Remove s[left] from window
                char = s[left]
                if char in need:
                    if need[char] == 0:  # About to lose a satisfied char
                        formed -= 1
                    need[char] += 1
                left += 1

        return result


# Test cases: list of (args_tuple, expected_output)
TEST_CASES = [
    (("ADOBECODEBANC", "ABC"), "BANC"),
    (("a", "a"), "a"),
    (("a", "aa"), ""),
    (("aa", "aa"), "aa"),
    (("abc", "b"), "b"),
    (("ab", "A"), ""),  # Case sensitive
]

METHOD_NAME = "minWindow"
