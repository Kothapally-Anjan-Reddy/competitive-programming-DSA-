# 0032 · Longest Valid Parentheses

**Platform:** LeetCode &nbsp;|&nbsp; **Difficulty:** Hard &nbsp;|&nbsp; [Problem link](https://leetcode.com/problems/longest-valid-parentheses/)

**Topics:** `String` `Dynamic Programming` `Stack` `Bracket Sequences`

## Accepted solutions

| Language | Runtime | Memory | Date | Submission |
| --- | --- | --- | --- | --- |
| [Python3](./solution.py) | 14 ms | 19.6 MB | 2026-10-07 | [link](https://leetcode.com/submissions/detail/2165520719/) |

## Problem

Given a string containing just the characters `'('` and `')'`, return *the length of the longest valid (well-formed) parentheses **substring*.

**Example 1:**

```
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
```

**Example 2:**

```
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
```

**Example 3:**

```
Input: s = ""
Output: 0
```

**Constraints:**

	- `0 <= s.length <= 3 * 10^4`

	- `s[i]` is `'('`, or `')'`.
