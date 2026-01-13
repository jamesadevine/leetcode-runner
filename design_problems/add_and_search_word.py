"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""


class WordDictionary:
    """
    Design Add and Search Words Data Structure (LeetCode #211)

    Design a data structure that supports adding new words and finding
    if a string matches any previously added string.

    Implement the WordDictionary class:
    - WordDictionary() Initializes the object.
    - void addWord(word) Adds word to the data structure, it can be matched later.
    - bool search(word) Returns true if there is any string in the data structure
      that matches word or false otherwise. word may contain dots '.' where dots
      can be matched with any letter.

    Example:
    Input: ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
           [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
    Output: [null,null,null,null,false,true,true,true]

    Constraints:
    - 1 <= word.length <= 25
    - word in addWord consists of lowercase English letters.
    - word in search consist of '.' or lowercase English letters.
    - There will be at most 2 dots in word for search queries.
    - At most 10^4 calls will be made to addWord and search.

    Approach: Trie with DFS for wildcard matching
    - addWord: standard Trie insert
    - search: DFS with branching on '.' (try all children)
    """

    def __init__(self):
        pass

    def addWord(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass


# This problem requires special handling - it's a class design problem
TEST_CASES = []
METHOD_NAME = None

# Manual test:
# wd = WordDictionary()
# wd.addWord("bad")
# wd.addWord("dad")
# wd.addWord("mad")
# wd.search("pad")  # False
# wd.search("bad")  # True
# wd.search(".ad")  # True
# wd.search("b..")  # True
