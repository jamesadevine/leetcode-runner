"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""


class LRUCache:
    """
    LRU Cache (LeetCode #146)

    Design a data structure that follows the constraints of a
    Least Recently Used (LRU) cache.

    Implement the LRUCache class:
    - LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    - int get(int key) Return the value of the key if the key exists,
      otherwise return -1.
    - void put(int key, int value) Update the value of the key if the key exists.
      Otherwise, add the key-value pair to the cache. If the number of keys
      exceeds the capacity from this operation, evict the least recently used key.

    The functions get and put must each run in O(1) average time complexity.

    Example:
    Input: ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
           [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    Output: [null, null, null, 1, null, -1, null, -1, 3, 4]

    Constraints:
    - 1 <= capacity <= 3000
    - 0 <= key <= 10^4
    - 0 <= value <= 10^5
    - At most 2 * 10^5 calls will be made to get and put.

    Approach: Hash Map + Doubly Linked List
    - Hash map: key -> node (O(1) lookup)
    - Doubly linked list: maintains order (O(1) move to front, remove from end)
    - get: lookup in map, move node to front (most recent)
    - put: add/update node, move to front, evict tail if over capacity
    """

    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass


# This problem requires special handling - it's a class design problem
TEST_CASES = []
METHOD_NAME = None

# Manual test:
# cache = LRUCache(2)
# cache.put(1, 1)
# cache.put(2, 2)
# cache.get(1)      # returns 1
# cache.put(3, 3)   # evicts key 2
# cache.get(2)      # returns -1 (not found)
# cache.put(4, 4)   # evicts key 1
# cache.get(1)      # returns -1 (not found)
# cache.get(3)      # returns 3
# cache.get(4)      # returns 4
