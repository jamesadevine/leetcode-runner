# LeetCode Concepts Reference

A summary of key concepts, patterns, and techniques for solving LeetCode problems.

---

## Data Structures

### Arrays & Strings
- **Two Pointers**: Use two indices moving toward each other or in the same direction
- **Sliding Window**: Maintain a window of elements, expand/contract as needed
- **Prefix Sum**: Precompute cumulative sums for O(1) range queries

### Linked Lists
- **Fast/Slow Pointers**: Detect cycles, find middle, find nth from end
- **Dummy Head**: Simplifies edge cases when head might change
- **Pointer Switching**: Traverse both lists to synchronize lengths (intersection problem)

### Hash Maps / Sets
- **Frequency Count**: Count occurrences of elements
- **Two Sum Pattern**: Store complements for O(1) lookup
- **Seen Set**: Track visited elements to avoid duplicates

### Stacks & Queues
- **Monotonic Stack**: Maintain increasing/decreasing order for "next greater" problems
- **BFS Queue**: Level-order traversal, shortest path in unweighted graphs
- **Valid Parentheses**: Match opening/closing with stack

### Trees
- **DFS Traversals**: Preorder, Inorder, Postorder (recursive or iterative)
- **BFS/Level Order**: Use queue, process level by level
- **Binary Search Tree**: In-order traversal gives sorted order

### Graphs
- **Adjacency List**: Standard representation for sparse graphs
- **DFS**: Explore deep, good for paths, cycles, connected components
- **BFS**: Explore wide, good for shortest path (unweighted)
- **Topological Sort**: Order dependencies (Kahn's algorithm or DFS)
- **Union-Find**: Track connected components efficiently

### Heaps (Priority Queues)
- **Top K Elements**: Use min-heap of size K
- **Merge K Sorted**: Use heap to track smallest across lists
- **Median Finding**: Two heaps (max-heap for lower half, min-heap for upper)

---

## Algorithmic Techniques

### Binary Search

Binary search eliminates half the search space with each comparison. It requires a **sorted** or **monotonic** structure.

**When to use:**
- Searching in sorted arrays
- Finding boundaries (first/last occurrence)
- "Minimum value that satisfies X" or "Maximum value that satisfies X"

**Key variants:**
| Variant | Use Case | Condition |
|---------|----------|-----------|
| Standard | Find exact match | `arr[mid] == target` |
| Lower Bound | First element ≥ target | Move `right = mid` when `arr[mid] >= target` |
| Upper Bound | First element > target | Move `left = mid + 1` when `arr[mid] <= target` |
| Search on Answer | Find min/max feasible value | Binary search the answer space, not the array |

**Example - Search on Answer:**
> "What's the minimum capacity to ship all packages in D days?"

Instead of searching an array, binary search the *capacity value* from min to max, checking if each capacity is feasible.

**Complexity:** O(log n)

---

### Dynamic Programming

DP solves problems by breaking them into overlapping subproblems and storing results to avoid recomputation.

**Two requirements:**
1. **Overlapping Subproblems**: Same subproblem solved multiple times
2. **Optimal Substructure**: Optimal solution built from optimal sub-solutions

**5-Step Framework:**
1. **Define the state**: What variables uniquely identify a subproblem?
   - `dp[i]` = answer for first `i` elements
   - `dp[i][j]` = answer for subproblem with parameters `i` and `j`
2. **Define the recurrence**: How do states relate?
   - `dp[i] = min(dp[i-1], dp[i-2]) + cost[i]`
3. **Identify base cases**: What's trivially known?
   - `dp[0] = 0`, `dp[1] = 1`
4. **Determine iteration order**: Ensure dependencies are computed first
5. **Extract the answer**: Usually `dp[n]` or `dp[n][m]`

**Two approaches:**

| Approach | Direction | Pros | Cons |
|----------|-----------|------|------|
| **Top-Down** (Memoization) | Big → Small | Natural recursive thinking, only computes needed states | Recursion overhead, stack limits |
| **Bottom-Up** (Tabulation) | Small → Big | No recursion overhead, often faster | Must compute all states, order matters |

**Common DP Patterns:**

| Pattern | State | Example Problems |
|---------|-------|------------------|
| **Linear** | `dp[i]` = answer for first i items | Climbing Stairs, House Robber, Maximum Subarray |
| **Two Sequence** | `dp[i][j]` = answer for first i of A, j of B | Longest Common Subsequence, Edit Distance |
| **Grid** | `dp[i][j]` = answer to reach cell (i,j) | Unique Paths, Minimum Path Sum, Dungeon Game |
| **Knapsack** | `dp[i][w]` = best value with i items, capacity w | 0/1 Knapsack, Coin Change, Partition Equal Subset |
| **Interval** | `dp[i][j]` = answer for subarray [i..j] | Burst Balloons, Matrix Chain, Palindrome Partitioning |
| **Bitmask** | `dp[mask]` = answer for subset represented by mask | Travelling Salesman, Assign Tasks |

**Recognizing DP problems:**
- "Count the number of ways..."
- "What's the minimum/maximum..."
- "Is it possible to..." (often yes/no DP)
- "Longest/shortest sequence that..."

**Handling impossible cases:**
Use `float('inf')` or `float('-inf')` as "poison" values that propagate through invalid paths.

---

### Greedy

Greedy makes the locally optimal choice at each step, hoping it leads to a global optimum.

**When greedy works:**
- Problem has **greedy choice property**: local optimal leads to global optimal
- Problem has **optimal substructure**: optimal solution contains optimal sub-solutions

**When greedy fails:**
- Coin Change with arbitrary denominations: `[1, 3, 4]` amount `6`
  - Greedy: 4+1+1 = 3 coins
  - Optimal: 3+3 = 2 coins

**Common greedy problems:**

| Problem | Greedy Strategy |
|---------|-----------------|
| Activity Selection | Pick earliest ending time |
| Fractional Knapsack | Pick highest value/weight ratio |
| Huffman Coding | Merge two smallest frequencies |
| Jump Game | Track farthest reachable position |
| Gas Station | If total gas ≥ total cost, start from first station where running sum goes negative |
| Candy Distribution | Two passes (left-to-right, right-to-left) |

**Proving greedy correctness:**
1. **Exchange argument**: Show swapping any choice with greedy choice doesn't improve solution
2. **Stays ahead**: Show greedy is never worse at any step

---

### Backtracking

Backtracking explores all possibilities by building solutions incrementally and abandoning ("backtracking") paths that can't lead to valid solutions.

**The pattern:**
```
1. Choose: Pick an option
2. Explore: Recurse with that choice
3. Unchoose: Undo the choice (backtrack)
```

**When to use:**
- Generate all permutations/combinations/subsets
- Constraint satisfaction (Sudoku, N-Queens)
- Path finding with constraints
- "Find all solutions that..."

**Pruning strategies:**
- Skip invalid choices early (don't recurse if already invalid)
- Use constraints to reduce search space
- Sort input to enable early termination

**Common backtracking problems:**

| Problem | Key Insight |
|---------|-------------|
| Subsets | Include or exclude each element |
| Permutations | Try each unused element at each position |
| Combinations | Choose k elements, avoid duplicates by only going forward |
| N-Queens | Place queen row by row, check column/diagonal conflicts |
| Sudoku | Fill cell by cell, validate row/col/box constraints |
| Word Search | DFS from each cell, mark visited |

**Time complexity:** Often O(n!) or O(2ⁿ) — exponential, but pruning helps in practice.

---

### Divide and Conquer

Split problem into independent subproblems, solve recursively, combine results.

**Structure:**
1. **Divide**: Break into smaller subproblems
2. **Conquer**: Solve subproblems recursively
3. **Combine**: Merge subproblem solutions

**Classic examples:**

| Algorithm | Divide | Combine | Complexity |
|-----------|--------|---------|------------|
| Merge Sort | Split array in half | Merge sorted halves | O(n log n) |
| Quick Sort | Partition around pivot | Concatenate | O(n log n) avg |
| Binary Search | Eliminate half | Return result | O(log n) |
| Median of Two Sorted Arrays | Compare medians | Recurse on half | O(log(m+n)) |

**Difference from DP:**
- Divide & Conquer: Subproblems are **independent** (no overlap)
- DP: Subproblems **overlap** (same subproblem solved multiple times)

---

### Two Pointers

Use two indices to traverse data, reducing O(n²) brute force to O(n).

**Variants:**

| Type | Setup | Use Case |
|------|-------|----------|
| **Opposite ends** | `left=0, right=n-1` | Two Sum (sorted), Container With Most Water, Valid Palindrome |
| **Same direction** | `slow=0, fast=0` | Remove duplicates, Linked list cycle, Sliding window |
| **Different arrays** | `i=0, j=0` | Merge sorted arrays, Intersection |

**When to use:**
- Sorted array + find pair with property
- In-place array modification
- Linked list problems (fast/slow)

---

### Sliding Window

Maintain a "window" over a contiguous subarray, expanding and contracting efficiently.

**Two types:**

| Type | When to use | Example |
|------|-------------|---------|
| **Fixed size** | Window size k is given | Max sum of k consecutive elements |
| **Variable size** | Find min/max window satisfying condition | Minimum window substring |

**Variable window strategy:**
1. Expand `right` to include more elements
2. While window is invalid (or optimal found), shrink from `left`
3. Update answer at valid states

**Common problems:**
- Longest substring without repeating characters
- Minimum window substring
- Maximum sum subarray of size k
- Longest subarray with sum ≤ k

---

### Recursion

**Mental model:** Assume the recursive call works correctly. Focus only on:
1. Base case: When to stop?
2. Recursive case: How to reduce to smaller problem?
3. Combination: How to use recursive result?

**Common pitfalls:**
- Missing base case → infinite recursion
- Not reducing problem size → infinite recursion
- Modifying shared state incorrectly → wrong results

**Recursion vs Iteration:**
- Every recursion can be converted to iteration (with explicit stack)
- Recursion often more elegant for tree/graph traversals
- Iteration avoids stack overflow for deep recursion

---

## Common Patterns

### Two Pointers
```python
left, right = 0, len(arr) - 1
while left < right:
    # process arr[left] and arr[right]
    # move pointers based on condition
```

### Sliding Window
```python
left = 0
for right in range(len(arr)):
    # expand window by including arr[right]
    while window_invalid:
        # shrink from left
        left += 1
    # update answer
```

### BFS Template
```python
from collections import deque
queue = deque([start])
visited = {start}
while queue:
    node = queue.popleft()
    for neighbor in get_neighbors(node):
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```

### DFS Template
```python
def dfs(node, visited):
    if node in visited:
        return
    visited.add(node)
    for neighbor in get_neighbors(node):
        dfs(neighbor, visited)
```

### Binary Search Template
```python
left, right = 0, len(arr) - 1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

### Backtracking Template
```python
def backtrack(path, choices):
    if is_solution(path):
        result.append(path[:])
        return
    for choice in choices:
        if is_valid(choice):
            path.append(choice)
            backtrack(path, remaining_choices)
            path.pop()  # undo
```

---

## Complexity Cheat Sheet

| Complexity | Name | Example |
|------------|------|---------|
| O(1) | Constant | Hash lookup, array index |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Single pass through array |
| O(n log n) | Linearithmic | Efficient sorting (merge, heap) |
| O(n²) | Quadratic | Nested loops, bubble sort |
| O(2ⁿ) | Exponential | Subsets, naive recursion |
| O(n!) | Factorial | Permutations |

---

## Problem-Solving Framework

1. **Understand**: Read carefully, identify inputs/outputs, clarify constraints
2. **Examples**: Work through examples by hand
3. **Pattern Match**: Does this look like a known problem type?
4. **Brute Force**: What's the naive solution? What's its complexity?
5. **Optimize**: Can you use a better data structure? Algorithm?
6. **Implement**: Write clean code, handle edge cases
7. **Test**: Verify with examples, think of edge cases

---

## Edge Cases to Consider

- Empty input
- Single element
- All same elements
- Already sorted / reverse sorted
- Negative numbers
- Integer overflow
- Null/None values
- Cycles (in graphs/linked lists)
