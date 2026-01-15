"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        Group Anagrams (LeetCode #49)

        Given an array of strings strs, group the anagrams together.
        You can return the answer in any order.

        An Anagram is a word or phrase formed by rearranging the letters
        of a different word or phrase, typically using all the original
        letters exactly once.

        Example 1:
        Input: strs = ["eat","tea","tan","ate","nat","bat"]
        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

        Example 2:
        Input: strs = [""]
        Output: [[""]]

        Example 3:
        Input: strs = ["a"]
        Output: [["a"]]

        Constraints:
        - 1 <= strs.length <= 10^4
        - 0 <= strs[i].length <= 100
        - strs[i] consists of lowercase English letters.
        """
        from collections import defaultdict

        out = defaultdict(list)

        for word in strs:
            out[tuple(sorted(word))].append(word)

        return list(out.values())


# Test cases: list of (args_tuple, expected_output)
# Note: Order doesn't matter, so test runner may need custom comparison
TEST_CASES = [
    (
        (["eat", "tea", "tan", "ate", "nat", "bat"],),
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
    ),
    (([""],), [[""]]),
    ((["a"],), [["a"]]),
    ((["", ""],), [["", ""]]),
    ((["abc", "cba", "bca", "xyz"],), [["abc", "cba", "bca"], ["xyz"]]),
]

# Name of the method to test
METHOD_NAME = "groupAnagrams"
