# 0215 · Kth Largest Element in an Array

**Platform:** LeetCode &nbsp;|&nbsp; **Difficulty:** Medium &nbsp;|&nbsp; [Problem link](https://leetcode.com/problems/kth-largest-element-in-an-array/)

**Topics:** `Array` `Divide and Conquer` `Sorting` `Heap (Priority Queue)` `Quickselect`

## Accepted solutions

| Language | Runtime | Memory | Date | Submission |
| --- | --- | --- | --- | --- |
| [Python3](./solution.py) | 91 ms | 29.8 MB | 2026-03-12 | [link](https://leetcode.com/submissions/detail/1946024622/) |

## Problem

Given an integer array `nums` and an integer `k`, return *the* `k^th` *largest element in the array*.

Note that it is the `k^th` largest element in the sorted order, not the `k^th` distinct element.

Can you solve it without sorting?

**Example 1:**

```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

**Example 2:**

```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

**Constraints:**

	- `1 <= k <= nums.length <= 10^5`

	- `-10^4 <= nums[i] <= 10^4`
