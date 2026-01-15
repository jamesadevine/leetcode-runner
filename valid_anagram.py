"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Valid Anagram (LeetCode #242)

        Given two strings s and t, return true if t is an anagram of s,
        and false otherwise.

        An Anagram is a word or phrase formed by rearranging the letters
        of a different word or phrase, typically using all the original
        letters exactly once.

        Example 1:
        Input: s = "anagram", t = "nagaram"
        Output: true

        Example 2:
        Input: s = "rat", t = "car"
        Output: false

        Constraints:
        - 1 <= s.length, t.length <= 5 * 10^4
        - s and t consist of lowercase English letters.

        Follow up: What if the inputs contain Unicode characters?
        How would you adapt your solution to such a case?
        """
        from collections import Counter

        freq_map_s = Counter(s)
        freq_map_t = Counter(t)

        return freq_map_s == freq_map_t


# Test cases: list of (args_tuple, expected_output)
TEST_CASES = [
    (("anagram", "nagaram"), True),
    (("rat", "car"), False),
    (("a", "a"), True),
    (("ab", "ba"), True),
    (("ab", "a"), False),
    (("aacc", "ccac"), False),
]

# Name of the method to test
METHOD_NAME = "isAnagram"
