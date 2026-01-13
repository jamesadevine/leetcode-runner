"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""


class MedianFinder:
    """
    Find Median from Data Stream (LeetCode #295)

    The median is the middle value in an ordered integer list. If the size
    of the list is even, there is no middle value, and the median is the
    mean of the two middle values.

    Implement the MedianFinder class:
    - MedianFinder() initializes the MedianFinder object.
    - void addNum(int num) adds the integer num from the data stream to
      the data structure.
    - double findMedian() returns the median of all elements so far.
      Answers within 10^-5 of the actual answer will be accepted.

    Example:
    Input: ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
           [[], [1], [2], [], [3], []]
    Output: [null, null, null, 1.5, null, 2.0]

    Constraints:
    - -10^5 <= num <= 10^5
    - There will be at least one element in the data structure before
      calling findMedian.
    - At most 5 * 10^4 calls will be made to addNum and findMedian.

    Follow up:
    - If all integer numbers from the stream are in the range [0, 100],
      how would you optimize your solution?
    - If 99% of all integer numbers from the stream are in the range [0, 100],
      how would you optimize your solution?

    Approach: Two Heaps
    - Max heap for lower half (negate values in Python)
    - Min heap for upper half
    - Keep heaps balanced (sizes differ by at most 1)
    - Median: top of larger heap, or average of both tops
    """

    def __init__(self):
        pass

    def addNum(self, num: int) -> None:
        pass

    def findMedian(self) -> float:
        pass


# This problem requires special handling - it's a class design problem
TEST_CASES = []
METHOD_NAME = None

# Manual test:
# mf = MedianFinder()
# mf.addNum(1)
# mf.addNum(2)
# mf.findMedian()  # 1.5
# mf.addNum(3)
# mf.findMedian()  # 2.0
