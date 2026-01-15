"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Valid Palindrome (LeetCode #125)

        A phrase is a palindrome if, after converting all uppercase letters
        into lowercase letters and removing all non-alphanumeric characters,
        it reads the same forward and backward. Alphanumeric characters
        include letters and numbers.

        Given a string s, return true if it is a palindrome, or false otherwise.

        Example 1:
        Input: s = "A man, a plan, a canal: Panama"
        Output: true
        Explanation: "amanaplanacanalpanama" is a palindrome.

        Example 2:
        Input: s = "race a car"
        Output: false
        Explanation: "raceacar" is not a palindrome.

        Example 3:
        Input: s = " "
        Output: true
        Explanation: s is an empty string "" after removing non-alphanumeric
        characters. Since an empty string reads the same forward and backward,
        it is a palindrome.

        Constraints:
        - 1 <= s.length <= 2 * 10^5
        - s consists only of printable ASCII characters.
        """
        s = "".join([c for c in s.lower() if c.isalnum()])

        n = len(s)

        if n == 0:
            return True

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True


# Test cases: list of (args_tuple, expected_output)
TEST_CASES = [
    (("A man, a plan, a canal: Panama",), True),
    (("race a car",), False),
    ((" ",), True),
    (("a",), True),
    (("ab",), False),
    ((".,",), True),
    (("0P",), False),
]

# Name of the method to test
METHOD_NAME = "isPalindrome"
