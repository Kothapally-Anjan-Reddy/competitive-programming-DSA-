# 0974 · Subarray Sums Divisible by K

**Platform:** LeetCode &nbsp;|&nbsp; **Difficulty:** Medium &nbsp;|&nbsp; [Problem link](https://leetcode.com/problems/subarray-sums-divisible-by-k/)

**Topics:** `Array` `Hash Table` `Prefix Sum`

## Accepted solutions

| Language | Runtime | Memory | Date | Submission |
| --- | --- | --- | --- | --- |
| [Python3](./solution.py) | 30 ms | 23.7 MB | 2026-10-22 | [link](https://leetcode.com/submissions/detail/2179064699/) |

## Problem

Given an integer array `nums` and an integer `k`, return *the number of non-empty **subarrays** that have a sum divisible by *`k`.

A **subarray** is a **contiguous** part of an array.

**Example 1:**

```
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
```

**Example 2:**

```
Input: nums = [5], k = 9
Output: 0
```

**Constraints:**

	- `1 <= nums.length <= 3 * 10^4`

	- `-10^4 <= nums[i] <= 10^4`

	- `2 <= k <= 10^4`
