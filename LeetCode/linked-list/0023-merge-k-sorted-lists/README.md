# 0023 · Merge k Sorted Lists

**Platform:** LeetCode &nbsp;|&nbsp; **Difficulty:** Hard &nbsp;|&nbsp; [Problem link](https://leetcode.com/problems/merge-k-sorted-lists/)

**Topics:** `Linked List` `Divide and Conquer` `Heap (Priority Queue)` `Merge Sort` `Tournament Sort`

## Accepted solutions

| Language | Runtime | Memory | Date | Submission |
| --- | --- | --- | --- | --- |
| [Python3](./solution.py) | 13 ms | 24.1 MB | 2026-10-28 | [link](https://leetcode.com/submissions/detail/2183913845/) |

## Problem

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

*Merge all the linked-lists into one sorted linked-list and return it.*

**Example 1:**

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
```

**Example 2:**

```
Input: lists = []
Output: []
```

**Example 3:**

```
Input: lists = [[]]
Output: []
```

**Constraints:**

	- `k == lists.length`

	- `0 <= k <= 10^4`

	- `0 <= lists[i].length <= 500`

	- `-10^4 <= lists[i][j] <= 10^4`

	- `lists[i]` is sorted in **ascending order**.

	- The sum of `lists[i].length` will not exceed `10^4`.
