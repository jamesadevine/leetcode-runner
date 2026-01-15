"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        """
        Word Break (LeetCode #139)

        Given a string s and a dictionary of strings wordDict, return true if s
        can be segmented into a space-separated sequence of one or more
        dictionary words.

        Note that the same word in the dictionary may be reused multiple times
        in the segmentation.

        Example 1:
        Input: s = "leetcode", wordDict = ["leet","code"]
        Output: true
        Explanation: Return true because "leetcode" can be segmented as "leet code".

        Example 2:
        Input: s = "applepenapple", wordDict = ["apple","pen"]
        Output: true
        Explanation: Return true because "applepenapple" can be segmented as
        "apple pen apple". Note that you are allowed to reuse a dictionary word.

        Example 3:
        Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
        Output: false

        Constraints:
        - 1 <= s.length <= 300
        - 1 <= wordDict.length <= 1000
        - 1 <= wordDict[i].length <= 20
        - s and wordDict[i] consist of only lowercase English letters.
        - All the strings of wordDict are unique.
        """
        dp = [False] * (len(s) + 1)

        # empty string can be segmented
        dp[0] = True

        for i in range(1, len(s) + 1):
            # find the position
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[len(s)]


# Test cases: list of (args_tuple, expected_output)
TEST_CASES = [
    (("leetcode", ["leet", "code"]), True),
    (("applepenapple", ["apple", "pen"]), True),
    (("catsandog", ["cats", "dog", "sand", "and", "cat"]), False),
    (("a", ["a"]), True),
    (("ab", ["a", "b"]), True),
    (("aaaaaaa", ["aaa", "aaaa"]), True),
    (("aaaaaaa", ["aaa", "aaab"]), False),
]

# Name of the method to test
METHOD_NAME = "wordBreak"
