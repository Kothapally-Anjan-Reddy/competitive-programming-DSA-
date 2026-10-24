# 0856 · Score of Parentheses

**Platform:** LeetCode &nbsp;|&nbsp; **Difficulty:** Medium &nbsp;|&nbsp; [Problem link](https://leetcode.com/problems/score-of-parentheses/)

**Topics:** `String` `Stack` `Bracket Sequences`

## Accepted solutions

| Language | Runtime | Memory | Date | Submission |
| --- | --- | --- | --- | --- |
| [Python3](./solution.py) | 0 ms | 19.3 MB | 2026-10-06 | [link](https://leetcode.com/submissions/detail/2164552738/) |

## Problem

Given a balanced parentheses string `s`, return *the **score** of the string*.

The **score** of a balanced parentheses string is based on the following rule:

	- `"()"` has score `1`.

	- `AB` has score `A + B`, where `A` and `B` are balanced parentheses strings.

	- `(A)` has score `2 * A`, where `A` is a balanced parentheses string.

**Example 1:**

```
Input: s = "()"
Output: 1
```

**Example 2:**

```
Input: s = "(())"
Output: 2
```

**Example 3:**

```
Input: s = "()()"
Output: 2
```

**Constraints:**

	- `2 <= s.length <= 50`

	- `s` consists of only `'('` and `')'`.

	- `s` is a balanced parentheses string.
