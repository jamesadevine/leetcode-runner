"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
"""

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = [1] * n

        # walk up the list first, handle left neighbour constraint
        for i in range(1, n):
            current_rating = ratings[i]
            if current_rating > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1

        # walk down the list next handle right neighbour constraint
        for i in range(n - 2, -1, -1):
            current_rating = ratings[i]

            if current_rating > ratings[i + 1]:
                candy[i] = max(candy[i], candy[i + 1] + 1)

        return sum(candy)


# Each args_tuple contains the arguments to pass to the method
TEST_CASES = [
    (
        ([1, 0, 2]),
        (5),
    ),
    (
        ([1, 2, 2]),
        (4),
    ),
]

# Name of the method to test
METHOD_NAME = "candy"
