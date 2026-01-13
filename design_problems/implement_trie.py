"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""


class Trie:
    """
    Implement Trie (Prefix Tree) (LeetCode #208)

    A trie (pronounced as "try") or prefix tree is a tree data structure
    used to efficiently store and retrieve keys in a dataset of strings.
    There are various applications of this data structure, such as
    autocomplete and spellchecker.

    Implement the Trie class:
    - Trie() Initializes the trie object.
    - void insert(String word) Inserts the string word into the trie.
    - boolean search(String word) Returns true if the string word is in
      the trie (i.e., was inserted before), and false otherwise.
    - boolean startsWith(String prefix) Returns true if there is a
      previously inserted string word that has the prefix prefix, and
      false otherwise.

    Example:
    Input: ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
           [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    Output: [null, null, true, false, true, null, true]

    Constraints:
    - 1 <= word.length, prefix.length <= 2000
    - word and prefix consist only of lowercase English letters.
    - At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.

    Approach:
    - Each node has a dictionary of children (char -> node)
    - Each node has an is_end flag to mark word endings
    - insert: traverse/create nodes for each char, mark end
    - search: traverse nodes, check is_end at final node
    - startsWith: traverse nodes, return True if path exists
    """

    def __init__(self):
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def startsWith(self, prefix: str) -> bool:
        pass


# This problem requires special handling - it's a class design problem
# The test cases below are for manual testing
TEST_CASES = []
METHOD_NAME = None

# Manual test:
# trie = Trie()
# trie.insert("apple")
# trie.search("apple")   # True
# trie.search("app")     # False
# trie.startsWith("app") # True
# trie.insert("app")
# trie.search("app")     # True
