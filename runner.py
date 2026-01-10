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


def values_equal(actual: Any, expected: Any) -> bool:
    """
    Compare two values for equality.
    Handles special cases like unordered list comparison.
    """
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

    if not hasattr(solution, method_name):
        print(f"❌ Error: Method '{method_name}' not found in Solution class")
        sys.exit(1)

    method = getattr(solution, method_name)
    print(f"🔧 Method: {method_name}")
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

        # Run the test
        start_time = time.perf_counter()
        try:
            actual = method(*args)
            elapsed = (time.perf_counter() - start_time) * 1000  # ms
            total_time += elapsed

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
            failed += 1
            elapsed = (time.perf_counter() - start_time) * 1000
            total_time += elapsed
            print(f"\nTest {i}: 💥 ERROR ({elapsed:.3f}ms)")
            print(f"  Input:    {format_value(args)}")
            print(f"  Expected: {format_value(expected)}")
            print(f"  Error:    {type(e).__name__}: {e}")

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
