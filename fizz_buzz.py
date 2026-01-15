"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""


class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        """
        Fizz Buzz (LeetCode #412)

        Given an integer n, return a string array answer (1-indexed) where:

        - answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
        - answer[i] == "Fizz" if i is divisible by 3.
        - answer[i] == "Buzz" if i is divisible by 5.
        - answer[i] == i (as a string) if none of the above conditions are true.

        Example 1:
        Input: n = 3
        Output: ["1","2","Fizz"]

        Example 2:
        Input: n = 5
        Output: ["1","2","Fizz","4","Buzz"]

        Example 3:
        Input: n = 15
        Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

        Constraints:
        - 1 <= n <= 10^4
        """
        out = []

        for i in range(1, n + 1):
            divisible_by_three = i % 3
            divisible_by_five = i % 5
            if divisible_by_five == 0 and divisible_by_three == 0:
                out.append("FizzBuzz")
            elif divisible_by_three == 0:
                out.append("Fizz")
            elif divisible_by_five == 0:
                out.append("Buzz")
            else:
                out.append(str(i))

        return out


# Test cases: list of (args_tuple, expected_output)
TEST_CASES = [
    ((3,), ["1", "2", "Fizz"]),
    ((5,), ["1", "2", "Fizz", "4", "Buzz"]),
    (
        (15,),
        [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz",
        ],
    ),
    ((1,), ["1"]),
]

# Name of the method to test
METHOD_NAME = "fizzBuzz"
