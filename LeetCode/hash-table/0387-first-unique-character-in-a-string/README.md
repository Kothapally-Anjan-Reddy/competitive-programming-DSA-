# 0387 · First Unique Character in a String

**Platform:** LeetCode &nbsp;|&nbsp; **Difficulty:** Easy &nbsp;|&nbsp; [Problem link](https://leetcode.com/problems/first-unique-character-in-a-string/)

**Topics:** `Hash Table` `String` `Queue` `Counting`

## Accepted solutions

| Language | Runtime | Memory | Date | Submission |
| --- | --- | --- | --- | --- |
| [Python3](./solution.py) | 95 ms | 19.7 MB | 2026-01-26 | [link](https://leetcode.com/submissions/detail/1897684293/) |

## Problem

Given a string `s`, find the **first** non-repeating character in it and return its index. If it **does not** exist, return `-1`.

**Example 1:**

**Input:** s = "leetcode"

**Output:** 0

**Explanation:**

The character `'l'` at index 0 is the first character that does not occur at any other index.

**Example 2:**

**Input:** s = "loveleetcode"

**Output:** 2

**Example 3:**

**Input:** s = "aabb"

**Output:** -1

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` consists of only lowercase English letters.
