# Binary Search

## Overview
Binary search is a divide-and-conquer algorithm that efficiently finds a target value in a **sorted** collection by repeatedly halving the search space.

- **Time Complexity**: O(log n)
- **Space Complexity**: O(1) iterative, O(log n) recursive

## Key Patterns

### 1. Standard Binary Search (Find Exact Match)
```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

### 2. Bisect Left (Lower Bound)
Find the **leftmost** position where target can be inserted (first element >= target).

```python
def bisect_left(nums, target):
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left
```

### 3. Bisect Right (Upper Bound)
Find the **rightmost** position where target can be inserted (first element > target).

```python
def bisect_right(nums, target):
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left
```

## Common Variations

### Find First/Last Occurrence
```python
# First occurrence of target
def find_first(nums, target):
    idx = bisect_left(nums, target)
    if idx < len(nums) and nums[idx] == target:
        return idx
    return -1

# Last occurrence of target
def find_last(nums, target):
    idx = bisect_right(nums, target) - 1
    if idx >= 0 and nums[idx] == target:
        return idx
    return -1
```

### Search on Answer Space
When the answer itself can be binary searched (minimize/maximize problems):

```python
def search_on_answer(lo, hi, is_feasible):
    """
    Find minimum value where is_feasible(x) returns True.
    Assumes: is_feasible is monotonic (False...False, True...True)
    """
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if is_feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

## Tips & Pitfalls

1. **Overflow prevention**: Use `mid = left + (right - left) // 2` instead of `(left + right) // 2`

2. **Loop condition**:
   - `while left <= right` for exact match (search space shrinks to 0)
   - `while left < right` for boundary finding (converges to single element)

3. **Boundary updates**:
   - Always ensure the search space shrinks: `left = mid + 1` or `right = mid - 1`
   - For `while left < right`, use `right = mid` (not `mid - 1`) to avoid skipping answer

4. **Off-by-one errors**: Be careful with `len(nums)` vs `len(nums) - 1` for initial `right`

## Classic LeetCode Problems

| # | Problem | Pattern |
|---|---------|---------|
| 704 | Binary Search | Standard |
| 35 | Search Insert Position | Bisect Left |
| 34 | Find First and Last Position | Bisect Left + Right |
| 69 | Sqrt(x) | Search on Answer |
| 153 | Find Minimum in Rotated Sorted Array | Modified Binary Search |
| 33 | Search in Rotated Sorted Array | Modified Binary Search |
| 875 | Koko Eating Bananas | Search on Answer |
| 1011 | Capacity To Ship Packages | Search on Answer |

## Python Built-in: bisect module

```python
import bisect

nums = [1, 3, 3, 3, 5, 7]

bisect.bisect_left(nums, 3)   # 1 (first position where 3 can be inserted)
bisect.bisect_right(nums, 3)  # 4 (after all existing 3s)
bisect.bisect(nums, 3)        # 4 (alias for bisect_right)

bisect.insort_left(nums, 4)   # Insert 4 at leftmost valid position
```
