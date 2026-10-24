# 0322 · Coin Change

**Platform:** LeetCode &nbsp;|&nbsp; **Difficulty:** Medium &nbsp;|&nbsp; [Problem link](https://leetcode.com/problems/coin-change/)

**Topics:** `Array` `Dynamic Programming` `Breadth-First Search` `Knapsack Problem` `Complete Knapsack`

## Accepted solutions

| Language | Runtime | Memory | Date | Submission |
| --- | --- | --- | --- | --- |
| [Python3](./solution.py) | 454 ms | 19.8 MB | 2026-09-27 | [link](https://leetcode.com/submissions/detail/2155309624/) |

## Problem

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the **fewest** number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

**Example 1:**

```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

**Example 2:**

```
Input: coins = [2], amount = 3
Output: -1
```

**Example 3:**

```
Input: coins = [1], amount = 0
Output: 0
```

**Constraints:**

	- `1 <= coins.length <= 12`

	- `1 <= coins[i] <= 2^31 - 1`

	- `0 <= amount <= 10^4`
