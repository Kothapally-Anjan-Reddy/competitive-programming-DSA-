# 0152 · Maximum Product Subarray

**Platform:** LeetCode &nbsp;|&nbsp; **Difficulty:** Medium &nbsp;|&nbsp; [Problem link](https://leetcode.com/problems/maximum-product-subarray/)

**Topics:** `Array` `Dynamic Programming`

## Accepted solutions

| Language | Runtime | Memory | Date | Submission |
| --- | --- | --- | --- | --- |
| [Python3](./solution.py) | 5 ms | 19.8 MB | 2026-10-12 | [link](https://leetcode.com/submissions/detail/2170163039/) |

## Problem

Given an integer array `nums`, find a subarray that has the largest product, and return *the product*.

The test cases are generated so that the answer will fit in a **32-bit** integer.

**Note** that the product of an array with a single element is the value of that element.

**​​​​​​​Example 1:**

```
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```

**Example 2:**

```
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```

**Constraints:**

	- `1 <= nums.length <= 2 * 10^4`

	- `-10 <= nums[i] <= 10`

	- The product of any subarray of `nums` is **guaranteed** to fit in a **32-bit** integer.
