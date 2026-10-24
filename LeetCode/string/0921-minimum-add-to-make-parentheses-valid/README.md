# 0921 · Minimum Add to Make Parentheses Valid

**Platform:** LeetCode &nbsp;|&nbsp; **Difficulty:** Medium &nbsp;|&nbsp; [Problem link](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)

**Topics:** `String` `Stack` `Greedy` `Bracket Sequences`

## Accepted solutions

| Language | Runtime | Memory | Date | Submission |
| --- | --- | --- | --- | --- |
| [Python3](./solution.py) | 3 ms | 19.1 MB | 2026-10-06 | [link](https://leetcode.com/submissions/detail/2164606964/) |

## Problem

A parentheses string is valid if and only if:

	- It is the empty string,

	- It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid strings, or

	- It can be written as `(A)`, where `A` is a valid string.

You are given a parentheses string `s`. In one move, you can insert a parenthesis at any position of the string.

	- For example, if `s = "()))"`, you can insert an opening parenthesis to be `"(**(**)))"` or a closing parenthesis to be `"())**)**)"`.

Return *the minimum number of moves required to make *`s`* valid*.

**Example 1:**

```
Input: s = "())"
Output: 1
```

**Example 2:**

```
Input: s = "((("
Output: 3
```

**Constraints:**

	- `1 <= s.length <= 1000`

	- `s[i]` is either `'('` or `')'`.
