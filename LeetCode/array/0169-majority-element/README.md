# 0169 · Majority Element

**Platform:** LeetCode &nbsp;|&nbsp; **Difficulty:** Easy &nbsp;|&nbsp; [Problem link](https://leetcode.com/problems/majority-element/)

**Topics:** `Array` `Hash Table` `Divide and Conquer` `Sorting` `Counting` `Boyer–Moore Majority Vote Algorithm`

## Accepted solutions

| Language | Runtime | Memory | Date | Submission |
| --- | --- | --- | --- | --- |
| [Python3](./solution.py) | 15 ms | 21.1 MB | 2026-05-29 | [link](https://leetcode.com/submissions/detail/2015964490/) |

## Problem

Given an array `nums` of size `n`, return *the majority element*.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

**Example 1:**

```
Input: nums = [3,2,3]
Output: 3
```

**Example 2:**

```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

**Constraints:**

	- `n == nums.length`

	- `1 <= n <= 5 * 10^4`

	- `-10^9 <= nums[i] <= 10^9`

	- The input is generated such that a majority element will exist in the array.

**Follow-up:** Could you solve the problem in linear time and in `O(1)` space?
