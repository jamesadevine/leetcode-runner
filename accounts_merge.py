"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""

from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        Accounts Merge (LeetCode #721)

        Given a list of accounts where each element accounts[i] is a list of
        strings, where the first element accounts[i][0] is a name, and the
        rest of the elements are emails representing emails of the account.

        Now, we would like to merge these accounts. Two accounts definitely
        belong to the same person if there is some common email to both accounts.
        Note that even if two accounts have the same name, they may belong to
        different people as people could have the same name.

        A person can have any number of accounts initially, but all of their
        accounts definitely have the same name.

        After merging the accounts, return the accounts in the following format:
        the first element of each account is the name, and the rest of the
        elements are emails in sorted order.

        Example 1:
        Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
                          ["John","johnsmith@mail.com","john00@mail.com"],
                          ["Mary","mary@mail.com"],
                          ["John","johnnybravo@mail.com"]]
        Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
                 ["John","johnnybravo@mail.com"],
                 ["Mary","mary@mail.com"]]

        Constraints:
        - 1 <= accounts.length <= 1000
        - 2 <= accounts[i].length <= 10
        - 1 <= accounts[i][j].length <= 30
        - accounts[i][0] consists of English letters.
        - accounts[i][j] (for j > 0) is a valid email.

        Approach: Union Find
        - Map each email to an index
        - Union emails within the same account
        - Group emails by their root, then format output
        """
        pass


# Test cases: list of (args_tuple, expected_output)
# Note: Output lists need to be sorted for comparison
TEST_CASES = [
    (
        (
            [
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["John", "johnsmith@mail.com", "john00@mail.com"],
                ["Mary", "mary@mail.com"],
                ["John", "johnnybravo@mail.com"],
            ],
        ),
        [
            ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
            ["John", "johnnybravo@mail.com"],
            ["Mary", "mary@mail.com"],
        ],
    ),
]

# Name of the method to test
METHOD_NAME = "accountsMerge"
