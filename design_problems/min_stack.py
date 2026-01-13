"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""


class MinStack:
    """
    Min Stack (LeetCode #155)

    Design a stack that supports push, pop, top, and retrieving the
    minimum element in constant time.

    Implement the MinStack class:
    - MinStack() initializes the stack object.
    - void push(int val) pushes the element val onto the stack.
    - void pop() removes the element on the top of the stack.
    - int top() gets the top element of the stack.
    - int getMin() retrieves the minimum element in the stack.

    You must implement a solution with O(1) time complexity for each function.

    Example:
    Input: ["MinStack","push","push","push","getMin","pop","top","getMin"]
           [[],[-2],[0],[-3],[],[],[],[]]
    Output: [null,null,null,null,-3,null,0,-2]

    Constraints:
    - -2^31 <= val <= 2^31 - 1
    - Methods pop, top and getMin operations will always be called on non-empty stacks.
    - At most 3 * 10^4 calls will be made to push, pop, top, and getMin.

    Approach: Two stacks or store (value, current_min) pairs
    - Option 1: Maintain a parallel min stack
    - Option 2: Each stack entry stores (value, min_at_this_point)
    """

    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def getMin(self) -> int:
        pass


# This problem requires special handling - it's a class design problem
TEST_CASES = []
METHOD_NAME = None

# Manual test:
# ms = MinStack()
# ms.push(-2)
# ms.push(0)
# ms.push(-3)
# ms.getMin()  # returns -3
# ms.pop()
# ms.top()     # returns 0
# ms.getMin()  # returns -2
