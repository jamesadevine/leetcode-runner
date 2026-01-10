# Problem

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

I need to come back to this.


Understanding k in the Median Algorithm
k represents the 0-based index of the element you're looking for in the hypothetically merged sorted array.

The Core Idea
Instead of actually merging the arrays (which would be O(m+n)), the algorithm uses binary search to find the k-th element in O(log(m+n)) time.

How k is Set Initially
For [1,3] and [2] (merged = [1,2,3], length 3):

k = 3 // 2 = 1 → find index 1 → value 2 ✓
For [1,2] and [3,4] (merged = [1,2,3,4], length 4):

Find indices 1 and 2 → values 2 and 3 → average = 2.5 ✓
The Key Insight: a_index + b_index < k
This condition asks: "Is k in the RIGHT half of the combined search space?"

a_index = midpoint of current A range
b_index = midpoint of current B range
a_index + b_index = how many elements are to the LEFT of both midpoints combined
If a_index + b_index < k: The k-th element is in the right portion → eliminate the smaller left half (we need to look further right)

If a_index + b_index >= k: The k-th element is in the left portion → eliminate the larger right half (we've gone too far right)

Why k - a_start and k - b_start in Base Cases?
When A is exhausted, a_start represents how many A elements were "used up" (eliminated from the left). So k - a_start gives the correct index into B for the remaining k-th position.

Visual Example
Arrays: A = [1, 5, 9], B = [2, 6, 10] → Find k=2 (the 3rd element, 0-indexed)

a_index=1 (value 5), b_index=1 (value 6)
1 + 1 = 2, which is NOT < k (2), so eliminate a right half
Since A[1]=5 < B[1]=6, eliminate right of B → b_end = 0
Continue recursing until finding the answer: 5
The algorithm essentially does a 2D binary search, using k as the target position to decide which half to eliminate each time.
