#!/usr/bin/env python3
"""
LeetCode Test Runner

Automatically runs test cases against your Solution class.
Usage: python runner.py [solution_file.py]
"""

import sys
import importlib.util
import time
from typing import Any
from pathlib import Path


def load_solution_module(filepath: str):
    """Dynamically load a solution module from file path."""
    spec = importlib.util.spec_from_file_location("solution", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def format_value(value: Any, max_length: int = 50) -> str:
    """Format a value for display, truncating if necessary."""
    s = repr(value)
    if len(s) > max_length:
        return s[: max_length - 3] + "..."
    return s


class ListNode:
    """Standard LeetCode ListNode for linked list problems."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next

    def __str__(self):
        curr = self
        text = "["
        while curr:
            text += f"{curr.val}, "
            curr = curr.next
        text += "]"
        return text


def list_to_linked(arr: list) -> "ListNode | None":
    """Convert a Python list to a linked list."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_to_list(head: "ListNode | None") -> list:
    """Convert a linked list to a Python list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def is_listnode(obj: Any) -> bool:
    """Check if an object is a ListNode (from any module)."""
    return obj is not None and type(obj).__name__ == "ListNode"


def values_equal(actual: Any, expected: Any) -> bool:
    """
    Compare two values for equality.
    Handles special cases like unordered list comparison and linked lists.
    """
    # Handle linked list comparison
    if is_listnode(actual) and is_listnode(expected):
        while actual and expected:
            if actual.val != expected.val:
                return False
            actual = actual.next
            expected = expected.next
        return actual is None and expected is None

    # For lists that represent unordered results (like two sum indices)
    # you might want to sort them before comparing
    if isinstance(actual, list) and isinstance(expected, list):
        # Try direct comparison first
        if actual == expected:
            return True
        # For problems where order doesn't matter, try sorted comparison
        try:
            return sorted(actual) == sorted(expected)
        except TypeError:
            return False
    return actual == expected


def run_tests(solution_file: str = "solution.py"):
    """Run all test cases from the solution file."""
    filepath = Path(solution_file)
    if not filepath.exists():
        print(f"❌ Error: File '{solution_file}' not found")
        sys.exit(1)

    print(f"📂 Loading: {filepath.name}")
    print("=" * 60)

    try:
        module = load_solution_module(str(filepath))
    except Exception as e:
        print(f"❌ Error loading module: {e}")
        sys.exit(1)

    # Get required attributes
    if not hasattr(module, "Solution"):
        print("❌ Error: No 'Solution' class found in module")
        sys.exit(1)

    if not hasattr(module, "TEST_CASES"):
        print("❌ Error: No 'TEST_CASES' list found in module")
        sys.exit(1)

    if not hasattr(module, "METHOD_NAME"):
        print("❌ Error: No 'METHOD_NAME' string found in module")
        sys.exit(1)

    solution = module.Solution()
    method_name = module.METHOD_NAME
    test_cases = module.TEST_CASES

    # Check for in-place modification flag
    inplace_arg_index = getattr(module, "INPLACE_ARG_INDEX", None)

    # Check for linked list args flag
    linked_list_args = getattr(module, "LINKED_LIST_ARGS", False)

    if not hasattr(solution, method_name):
        print(f"❌ Error: Method '{method_name}' not found in Solution class")
        sys.exit(1)

    method = getattr(solution, method_name)
    print(f"🔧 Method: {method_name}")
    if inplace_arg_index is not None:
        print(f"📌 In-place modification: arg[{inplace_arg_index}]")
    if linked_list_args:
        print(f"🔗 Linked list conversion enabled")
    print(f"📝 Test cases: {len(test_cases)}")
    print("=" * 60)

    passed = 0
    failed = 0
    total_time = 0

    for i, test_case in enumerate(test_cases, 1):
        args, expected = test_case

        # Handle both tuple and single argument
        if not isinstance(args, tuple):
            args = (args,)

        # Deep copy args for in-place problems (so original test cases aren't mutated)
        import copy

        args = tuple(copy.deepcopy(arg) for arg in args)

        # Convert list args to linked lists if needed
        if linked_list_args:
            args = tuple(
                list_to_linked(arg) if isinstance(arg, list) else arg for arg in args
            )

        # Run the test
        start_time = time.perf_counter()
        try:
            result = method(*args)
            elapsed = (time.perf_counter() - start_time) * 1000  # ms
            total_time += elapsed

            # For in-place modifications, check the modified argument instead of return value
            if inplace_arg_index is not None:
                actual = args[inplace_arg_index]
            else:
                actual = result

            # Convert linked list result to list for comparison if needed
            if linked_list_args and is_listnode(actual):
                actual = linked_to_list(actual)

            if values_equal(actual, expected):
                passed += 1
                status = "✅ PASS"
            else:
                failed += 1
                status = "❌ FAIL"

            print(f"\nTest {i}: {status} ({elapsed:.3f}ms)")
            print(f"  Input:    {format_value(args)}")
            print(f"  Expected: {format_value(expected)}")
            print(f"  Actual:   {format_value(actual)}")

        except Exception as e:
            import traceback

            failed += 1
            elapsed = (time.perf_counter() - start_time) * 1000
            total_time += elapsed
            print(f"\nTest {i}: 💥 ERROR ({elapsed:.3f}ms)")
            print(f"  Input:    {format_value(args)}")
            print(f"  Expected: {format_value(expected)}")
            print(f"  Error:    {type(e).__name__}: {e}")
            print(f"  Traceback:")
            # Print the full traceback, indented for readability
            for line in traceback.format_exception(type(e), e, e.__traceback__):
                for subline in line.rstrip().split("\n"):
                    print(f"    {subline}")

    # Summary
    print("\n" + "=" * 60)
    print(f"📊 Results: {passed}/{len(test_cases)} passed")
    print(f"⏱️  Total time: {total_time:.3f}ms")

    if failed == 0:
        print("🎉 All tests passed!")
    else:
        print(f"😢 {failed} test(s) failed")

    return failed == 0


if __name__ == "__main__":
    solution_file = sys.argv[1] if len(sys.argv) > 1 else "two_sum.py"
    success = run_tests(solution_file)
    sys.exit(0 if success else 1)
