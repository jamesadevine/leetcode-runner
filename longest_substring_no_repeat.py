"""
Longest Substring Without Repeating Characters (LeetCode #3)

Given a string s, find the length of the longest substring without repeating characters.

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
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        seen = set()

        for right in range(len(s)):
            # remove everything in the seen window up to and including the duplicate!!!
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            max_len = max(right - left + 1, max_len)

        return max_len

    # this is not a sliding window apparently
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     longest_substring = ""
    #     for window_len in range(1, len(s)):
    #         for i in range(len(s) - window_len):
    #             substring = s[i : i + window_len]

    #             vals = {}
    #             valid = True
    #             for v in substring:
    #                 if v in vals:
    #                     valid = False
    #                     break
    #                 vals[v] = 1

    #             if valid and window_len > len(longest_substring):
    #                 longest_substring = substring

    #     return len(longest_substring)


TEST_CASES = [
    # Example 1
    (("abcabcbb",), 3),
    # Example 2
    (("bbbbb",), 1),
    # Example 3
    (("pwwkew",), 3),
    # Edge case: empty string
    (("",), 0),
]

METHOD_NAME = "lengthOfLongestSubstring"
