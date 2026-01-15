"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Longest Substring Without Repeating Characters (LeetCode #3)

        Given a string s, find the length of the longest substring
        without repeating characters.

        Example 1:
        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.

        Example 2:
        Input: s = "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.

        Example 3:
        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a subsequence
        and not a substring.

        Constraints:
        - 0 <= s.length <= 5 * 10^4
        - s consists of English letters, digits, symbols and spaces.
        """

        # sliding window

        left = 0
        longest_length = 0
        n = len(s)
        seen = set()
        for right in range(n):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            longest_length = max(longest_length, right - left + 1)

        return longest_length


# Test cases: list of (args_tuple, expected_output)
TEST_CASES = [
    (("abcabcbb",), 3),
    (("bbbbb",), 1),
    (("pwwkew",), 3),
    (("",), 0),
    (("a",), 1),
    (("au",), 2),
    (("dvdf",), 3),
]

# Name of the method to test
METHOD_NAME = "lengthOfLongestSubstring"
