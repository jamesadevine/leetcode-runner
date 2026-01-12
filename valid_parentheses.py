"""
#20 - Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Approach: Stack
- Push opening brackets onto stack
- For closing brackets, check if top of stack matches
- At end, stack should be empty

Time: O(n)
Space: O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # TODO: Implement your solution
        # Hint: Use a stack and a mapping of closing -> opening brackets
        pass


# Test cases: list of (args_tuple, expected_output)
TEST_CASES = [
    (("()",), True),
    (("()[]{}",), True),
    (("(]",), False),
    (("([])",), True),
    (("([)]",), False),
    (("{[]}",), True),
    (("",), True),
    (("(",), False),
    ((")",), False),
]

METHOD_NAME = "isValid"
