# 0739 · Daily Temperatures

**Platform:** LeetCode &nbsp;|&nbsp; **Difficulty:** Medium &nbsp;|&nbsp; [Problem link](https://leetcode.com/problems/daily-temperatures/)

**Topics:** `Array` `Stack` `Monotonic Stack`

## Accepted solutions

| Language | Runtime | Memory | Date | Submission |
| --- | --- | --- | --- | --- |
| [Python3](./solution.py) | 135 ms | 36.2 MB | 2026-08-15 | [link](https://leetcode.com/submissions/detail/2107426408/) |

## Problem

Given an array of integers `temperatures` represents the daily temperatures, return *an array* `answer` *such that* `answer[i]` *is the number of days you have to wait after the* `i^th` *day to get a warmer temperature*. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

**Example 1:**

```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

**Example 2:**

```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

**Example 3:**

```
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

**Constraints:**

	- `1 <= temperatures.length <= 10^5`

	- `30 <= temperatures[i] <= 100`
