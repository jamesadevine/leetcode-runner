"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""

from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Word Search II (LeetCode #212)

        Given an m x n board of characters and a list of strings words,
        return all words on the board.

        Each word must be constructed from letters of sequentially adjacent
        cells, where adjacent cells are horizontally or vertically neighboring.
        The same letter cell may not be used more than once in a word.

        Example 1:
        Input: board = [["o","a","a","n"],
                        ["e","t","a","e"],
                        ["i","h","k","r"],
                        ["i","f","l","v"]],
               words = ["oath","pea","eat","rain"]
        Output: ["eat","oath"]

        Example 2:
        Input: board = [["a","b"],["c","d"]], words = ["abcb"]
        Output: []

        Constraints:
        - m == board.length
        - n == board[i].length
        - 1 <= m, n <= 12
        - board[i][j] is a lowercase English letter.
        - 1 <= words.length <= 3 * 10^4
        - 1 <= words[i].length <= 10
        - words[i] consists of lowercase English letters.
        - All the strings of words are unique.

        Approach: Trie + Backtracking
        - Build a Trie from all words
        - DFS from each cell, following Trie paths
        - Prune branches when no Trie path exists
        - Remove found words from Trie to avoid duplicates
        """
        pass


# Test cases: list of (args_tuple, expected_output)
TEST_CASES = [
    (
        (
            [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            ["oath", "pea", "eat", "rain"],
        ),
        ["eat", "oath"],
    ),
    (([["a", "b"], ["c", "d"]], ["abcb"]),),
]

# Name of the method to test
METHOD_NAME = "findWords"
