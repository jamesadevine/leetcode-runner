"""
LeetCode Solution Template

Write your solution class below. The test runner will automatically
invoke the specified method with your test cases.
"""

from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Task Scheduler (LeetCode #621)

        You are given an array of CPU tasks, each represented by letters A to Z,
        and a cooling time n. Each cycle or interval allows the completion of
        one task. Tasks can be completed in any order, but there's a constraint:
        identical tasks must be separated by at least n intervals due to cooling time.

        Return the minimum number of intervals required to complete all tasks.

        Example 1:
        Input: tasks = ["A","A","A","B","B","B"], n = 2
        Output: 8
        Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
        After completing task A, you must wait two cycles before doing A again.
        The same applies to task B. In the 3rd interval, neither A nor B can be done,
        so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

        Example 2:
        Input: tasks = ["A","A","A","B","B","B"], n = 0
        Output: 6
        Explanation: On this case any permutation of size 6 would work since n = 0.

        Example 3:
        Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
        Output: 16

        Constraints:
        - 1 <= tasks.length <= 10^4
        - tasks[i] is an uppercase English letter.
        - 0 <= n <= 100
        """

        pass

        # if n == 0:
        #     return len(tasks)

        # # at symbol represents idle task
        # idle_task = "@"
        # task_len = len(tasks)
        # result = task_len + 1  # out of range of possible min n

        # def schedule(
        #     previous_tasks: List[str], remaining_tasks: List[str], idle_count: int
        # ):
        #     nonlocal result
        #     if remaining_tasks == []:
        #         if idle_count < result:
        #             result = idle_count + len(tasks)
        #         return

        #     i = 0
        #     while i < len(remaining_tasks) and remaining_tasks[i] in previous_tasks:
        #         i += 1
        #     next_task = remaining_tasks[i] if i < len(remaining_tasks) else None

        #     # bump from the window
        #     previous_tasks.pop()

        #     if next_task is None:
        #         idle_count += 1
        #         next_task = idle_task
        #     else:
        #         remaining_tasks = remaining_tasks[:i] + remaining_tasks[i + 1 :]

        #     schedule([next_task] + previous_tasks, remaining_tasks, idle_count)

        # schedule([idle_task for _ in range(n)], tasks, 0)
        # return result


# Test cases: list of (args_tuple, expected_output)
TEST_CASES = [
    ((["A", "A", "A", "B", "B", "B"], 2), 8),
    ((["A", "A", "A", "B", "B", "B"], 0), 6),
    ((["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2), 16),
]

# Name of the method to test
METHOD_NAME = "leastInterval"
