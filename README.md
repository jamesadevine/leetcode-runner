# LeetCode Practice

A simple local environment for solving LeetCode problems in Python.

## Quick Start

1. Edit `solution.py` with your solution
2. Run tests: `python runner.py`

## File Structure

- `solution.py` - Your solution template (edit this)
- `runner.py` - Test runner script

## How to Use

### 1. Write Your Solution

Edit `solution.py` with your LeetCode solution:

```python
class Solution:
    def yourMethod(self, param1: int, param2: List[int]) -> int:
        # Your solution here
        pass

# Define test cases: (input_args, expected_output)
TEST_CASES = [
    ((arg1, arg2), expected_result),
    ((arg1, arg2), expected_result),
]

# Specify which method to test
METHOD_NAME = "yourMethod"
```

### 2. Run Tests

```bash
python runner.py              # Run solution.py
python runner.py my_solution.py  # Run specific file
```

## Example Output

```
📂 Loading: solution.py
============================================================
🔧 Method: twoSum
📝 Test cases: 3
============================================================

Test 1: ✅ PASS (0.015ms)
  Input:    ([2, 7, 11, 15], 9)
  Expected: [0, 1]
  Actual:   [0, 1]

...

============================================================
📊 Results: 3/3 passed
⏱️  Total time: 0.045ms
🎉 All tests passed!
```

## Tips

- Copy the method signature directly from LeetCode
- Add common imports at the top of `solution.py`
- Test cases are tuples of `(args, expected)` where args is a tuple of method arguments
