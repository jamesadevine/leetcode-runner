# Sorted Array Techniques

When you see a sorted array, two main techniques should come to mind:

## 🔍 Binary Search - "Find one specific thing"
- Looking for a single element
- Finding insertion point
- "Does X exist?"
- **O(log n)**

## 👆👆 Two Pointers - "Find a pair/relationship"
- Find two numbers that sum to X
- Container with most water
- Trapping rain water
- Comparing elements from both ends
- **O(n)**

---

## Quick Mental Checklist

| Situation | Technique |
|---|---|
| Find one value | Binary search |
| Find a pair with some sum/property | Two pointers |
| Find triplet/quadruplet | Fixed element + two pointers |
| Merge two sorted arrays | Two pointers (one per array) |
| Remove duplicates in-place | Two pointers (read/write) |
| Sliding window (subarray problems) | Two pointers (both moving right) |

---

## Why Two Pointers Works on Sorted Arrays

Two pointers on a sorted array works because moving a pointer has a **predictable effect** on the result:
- Move left pointer right → sum increases
- Move right pointer left → sum decreases

That predictability is what makes the technique powerful.

---

## When to Use Each

**Two Pointers wins when:**
- Array is already sorted (free!)
- Need to find pairs/relationships
- Space constraint (O(1) vs hash map's O(n))

**Hash Map wins when:**
- Array is unsorted
- No space constraint
- Sorting would add unnecessary O(n log n)

---

## Related Problems
- #1 Two Sum (unsorted → hash map)
- #167 Two Sum II (sorted → two pointers)
- #15 3Sum (sort + fixed element + two pointers)
- #16 3Sum Closest
- #18 4Sum
