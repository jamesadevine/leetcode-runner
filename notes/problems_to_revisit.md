# Problems to Revisit

Based on quiz session - January 13, 2026

---

## ❌ Valid Parentheses
**Mistake:** Suggested set + backtracking
**Correct approach:** Use a **stack**
- Push opening brackets onto stack
- When closing bracket appears, check if top of stack is matching opener
- Pop if match, return false if not
- Stack must be empty at end

**Why not a set?** Sets don't preserve order—you need LIFO to match the *most recent* unmatched bracket.

**Why not backtracking?** No branching/choices to explore—each closer has exactly one bracket it must match.

---

## ⚠️ Longest Increasing Subsequence (O(n log n) approach)
**Known:** O(n²) DP approach ✓
**To learn:** O(n log n) binary search approach

**Patience Sorting / Greedy + Binary Search:**
- Maintain array `tails` where `tails[i]` = smallest tail of all increasing subsequences of length `i+1`
- For each num: binary search `tails` to find first element ≥ num
  - If found: replace it (smaller tail for that length)
  - If not found: append (extend longest subsequence)
- `tails` stays sorted, enabling binary search
- Answer = `len(tails)`

**Key insight:** `tails` is NOT the actual LIS—it tracks optimal tail values to maximize extension potential.

---

## ❌ Median of Two Sorted Arrays
**Mistake:** Didn't know binary search criteria
**Correct approach:** Binary search on **partition position**

**Goal:** Partition both arrays so:
- Left side has `(m + n + 1) / 2` elements total
- All left elements ≤ all right elements

**Binary search on:** Partition index `i` of the smaller array
**Derived:** `j = (m + n + 1) / 2 - i` for the other array

**Valid partition condition:**
- `nums1[i-1] <= nums2[j]`
- `nums2[j-1] <= nums1[i]`

**Adjusting:**
- If `nums1[i-1] > nums2[j]` → move i left
- If `nums2[j-1] > nums1[i]` → move i right

**Median:**
- Odd: `max(nums1[i-1], nums2[j-1])`
- Even: `(max(left sides) + min(right sides)) / 2`

**Time:** O(log(min(m, n)))

---

## ⚠️ Course Schedule (Cycle Detection in Directed Graph)
**Known:** Directed graph + cycle detection ✓
**To learn:** Simple visited set isn't enough for directed graphs

**Why not just a visited set?**
```
A → B → C
↓
D → C
```
With just visited set, reaching C from D after visiting it from B looks like a cycle—but it's not!

**Approach 1: DFS with THREE states**
- `0` = unvisited
- `1` = visiting (in current recursion stack)
- `2` = visited (fully processed)
- **Cycle exists if** you encounter a node with state `1`

**Approach 2: BFS - Kahn's Algorithm (Topological Sort)**
- Calculate in-degree for each node
- Add nodes with in-degree `0` to queue
- Process queue: reduce neighbors' in-degrees, add to queue when they hit `0`
- **Cycle exists if** you can't process all nodes

**Time:** O(V + E)

---

## 🔄 Trapping Rain Water (Practice)
**Status:** Solved ✓ — added for reinforcement

**Key insight:** Water at position `i` = `min(maxLeft, maxRight) - height[i]`

**DP Approach:**
- **Base cases:** `maxLeft[0] = height[0]`, `maxRight[n-1] = height[n-1]`
- **Recurrence:**
  - `maxLeft[i] = max(maxLeft[i-1], height[i])` (left → right)
  - `maxRight[i] = max(maxRight[i+1], height[i])` (right → left)
- **Answer:** `sum(min(maxLeft[i], maxRight[i]) - height[i])`

**Time:** O(n), **Space:** O(n)

**Bonus - Two Pointer O(1) space:**
- Use `left` and `right` pointers with `maxLeft` and `maxRight` as single variables
- Move the pointer on the smaller side inward (that side is the bottleneck)

---

## Summary
| Problem | Status | Issue |
|---------|--------|-------|
| Valid Parentheses | ❌ | Wrong data structure (use stack) |
| LIS | ⚠️ | Learn O(n log n) binary search approach |
| Median of Two Sorted Arrays | ❌ | Learn partition-based binary search |
| Course Schedule | ⚠️ | Need 3-state DFS or Kahn's algorithm |
| Trapping Rain Water | 🔄 | Practice reinforcement |
