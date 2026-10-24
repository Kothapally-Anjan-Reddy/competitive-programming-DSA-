# 0416 · Partition Equal Subset Sum

**Platform:** LeetCode &nbsp;|&nbsp; **Difficulty:** Medium &nbsp;|&nbsp; [Problem link](https://leetcode.com/problems/partition-equal-subset-sum/)

**Topics:** `Array` `Dynamic Programming` `Knapsack Problem` `0-1 Knapsack`

## Accepted solutions

| Language | Runtime | Memory | Date | Submission |
| --- | --- | --- | --- | --- |
| [Python3](./solution.py) | 299 ms | 20.7 MB | 2026-10-13 | [link](https://leetcode.com/submissions/detail/2171384817/) |

## Problem

Given an integer array `nums`, return `true` *if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or *`false`* otherwise*.

**Example 1:**

```
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
```

**Example 2:**

```
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
```

**Constraints:**

	- `1 <= nums.length <= 200`

	- `1 <= nums[i] <= 100`
