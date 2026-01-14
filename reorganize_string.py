"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""


class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        Reorganize String (LeetCode #767)

        Given a string s, rearrange the characters of s so that any two
        adjacent characters are not the same.

        Return any possible rearrangement of s or return "" if not possible.

        Example 1:
        Input: s = "aab"
        Output: "aba"

        Example 2:
        Input: s = "aaab"
        Output: ""
        Explanation: No valid arrangement - 'a' appears too many times.

        Constraints:
        - 1 <= s.length <= 500
        - s consists of lowercase English letters.

        Key Insight (same as Task Scheduler!):
        - The most frequent character is the bottleneck
        - If max_freq > (len(s) + 1) // 2, it's impossible
        - Why? In "a_a_a_a" pattern, you can fit at most ceil(n/2) of one char

        Approaches:
        1. Greedy + Heap: Always place the most frequent char that isn't the previous
        2. Fill even indices first: Place most frequent at 0,2,4,... then fill odds
        """
        from collections import Counter
        import heapq

        reorganized_string = ""

        occurrence_map = Counter(s)

        max_freq = max(occurrence_map.values())

        heap = []

        if (len(s) + 1) / 2 >= max_freq:
            prev = None

            # build the max heap
            for s in occurrence_map:
                heapq.heappush(heap, (-occurrence_map[s], s))

            while len(heap) > 1:
                freq, character = heapq.heappop(heap)

                if prev != character:
                    reorganized_string += character
                    prev = character
                    freq += 1
                else:
                    freq1, character1 = heapq.heappop(heap)
                    reorganized_string += character1
                    prev = character1
                    freq1 += 1
                    if freq1 != 0:
                        heapq.heappush(heap, (freq1, character1))
                if freq != 0:
                    heapq.heappush(heap, (freq, character))

            # one element remains
            _, character = heapq.heappop(heap)
            reorganized_string += character

        return reorganized_string


# Test cases: list of (args_tuple, expected_output)
# Note: Multiple valid outputs possible, test runner may need custom validation
TEST_CASES = [
    (("aab",), "aba"),  # or "baa" is NOT valid, "aba" is
    (("aaab",), ""),
    (("vvvlo",), "vlvov"),  # or any valid arrangement
]

# Name of the method to test
METHOD_NAME = "reorganizeString"
