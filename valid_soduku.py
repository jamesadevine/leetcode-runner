"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

from typing import List


class Solution:
    def isValidSoduku(self, board: List[List[str]]) -> bool:
        BOARD_DIMS = 9
        cols = [set() for _ in range(BOARD_DIMS)]
        rows = [set() for _ in range(BOARD_DIMS)]
        boxes = [set() for _ in range(BOARD_DIMS)]

        for row in range(9):
            for col in range(9):
                print(f"{row} {col}")
                num = board[row][col]

                if num == ".":
                    continue

                box_index = ((row // 3) * 3) + (col // 3)

                if num in cols[col]:
                    print(f"invalid col: {num} {row} {col} {cols[col]}")
                    return False
                else:
                    cols[col].add(num)

                if num in rows[row]:
                    print("invalid row")
                    return False
                else:
                    rows[row].add(num)

                if num in boxes[box_index]:
                    print("invalid box")
                    return False
                else:
                    boxes[box_index].add(num)

        return True


# Test cases: list of (args_tuple, expected_output)
# Each args_tuple contains the arguments to pass to the method
TEST_CASES = [
    (
        (
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        ),
        True,
    ),
    (
        (
            [
                ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        ),
        False,
    ),
]

# Name of the method to test
METHOD_NAME = "isValidSoduku"
