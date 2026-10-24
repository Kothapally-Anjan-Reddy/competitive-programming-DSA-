# 0051 · N-Queens

**Platform:** LeetCode &nbsp;|&nbsp; **Difficulty:** Hard &nbsp;|&nbsp; [Problem link](https://leetcode.com/problems/n-queens/)

**Topics:** `Array` `Backtracking` `Algorithm X`

## Accepted solutions

| Language | Runtime | Memory | Date | Submission |
| --- | --- | --- | --- | --- |
| [Python3](./solution.py) | 7 ms | 19.6 MB | 2026-08-29 | [link](https://leetcode.com/submissions/detail/2124307893/) |

## Problem

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return *all distinct solutions to the **n-queens puzzle***. You may return the answer in **any order**.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/13/queens.jpg)

```
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
```

**Example 2:**

```
Input: n = 1
Output: [["Q"]]
```

**Constraints:**

	- `1 <= n <= 9`
