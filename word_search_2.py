"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}  # char → TrieNode
        self.word = None

    def __str__(self):
        return f"{self.children} {self.word}"


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
        """

        cols = len(board[0])
        rows = len(board)

        results = []

        root = TrieNode()
        for word in words:
            node = root

            # for each character in the word, descend and store the next character
            # at the end store the word, so when the final node is visited we know the word
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        def search_word(row: int, col: int, node: TrieNode):
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return

            char = board[row][col]

            if char not in node.children:
                return

            node = node.children[char]

            if node.word and node.word not in results:
                results.append(node.word)
                node.word = None
                # don't return here because the found word may be a sub word?

            board[row][col] = "#"
            search_word(row + 1, col, node)
            search_word(row - 1, col, node)
            search_word(row, col + 1, node)
            search_word(row, col - 1, node)
            board[row][col] = char

        for row in range(rows):
            for col in range(cols):
                search_word(row, col, root)

        return results


# Test cases: list of (args_tuple, expected_output)
TEST_CASES = [
    # Basic example from problem
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
    # No matches
    (([["a", "b"], ["c", "d"]], ["abcb"]), []),
    # Subwords: "art" is prefix of "artist"
    (
        (
            [
                ["a", "r", "t", "i"],
                ["x", "x", "s", "s"],
                ["x", "x", "t", "t"],
            ],
            ["art", "artist"],
        ),
        ["art", "artist"],
    ),
    # Subwords: "a" → "ab" → "abc" (nested prefixes)
    (
        (
            [
                ["a", "b", "c"],
            ],
            ["a", "ab", "abc"],
        ),
        ["a", "ab", "abc"],
    ),
    # Same word findable from multiple paths - should only appear once
    (
        (
            [
                ["a", "a"],
                ["a", "a"],
            ],
            ["aa", "aaa"],
        ),
        ["aa", "aaa"],
    ),
    # Longer word contains shorter: "the" vs "there" vs "thereafter"
    (
        (
            [
                ["t", "h", "e", "r", "e"],
                ["x", "x", "a", "f", "t"],
                ["x", "x", "e", "r", "x"],
            ],
            ["the", "there", "thereafter", "her"],
        ),
        ["the", "there", "her"],
    ),
    # Word requires backtracking path (can't just go straight)
    (
        (
            [
                ["a", "b"],
                ["c", "d"],
            ],
            ["acdb", "abcd", "abdc"],
        ),
        ["abdc", "acdb"],
    ),
    # Empty results - words exist but not on board
    (
        (
            [
                ["x", "y", "z"],
            ],
            ["abc", "def"],
        ),
        [],
    ),
    # Single cell board
    (([["a"]], ["a", "b", "aa"]), ["a"]),
]

# Name of the method to test
METHOD_NAME = "findWords"
