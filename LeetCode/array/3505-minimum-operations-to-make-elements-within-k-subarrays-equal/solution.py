import heapq
from collections import defaultdict

class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        cost = [0] * n
        
        # Two-Heap state for sliding window median
        small, large = [], []  # Max-heap (negated) and Min-heap
        sum_s = sum_l = 0
        cnt_s = cnt_l = 0
        del_map = defaultdict(int)

        def prune(h, is_small):
            while h:
                val = -h[0] if is_small else h[0]
                if del_map[val] > 0:
                    del_map[val] -= 1
                    heapq.heappop(h)
                else:
                    break

        def balance():
            nonlocal cnt_s, cnt_l, sum_s, sum_l
            target_s = (x + 1) // 2
            if cnt_s > target_s:
                val = -heapq.heappop(small)
                heapq.heappush(large, val)
                sum_s -= val; sum_l += val
                cnt_s -= 1; cnt_l += 1
                prune(small, True)
            elif cnt_s < target_s and large:
                val = heapq.heappop(large)
                heapq.heappush(small, -val)
                sum_l -= val; sum_s += val
                cnt_l -= 1; cnt_s += 1
                prune(large, False)

        # 1. Sliding Window Median Cost Calculation
        for i, num in enumerate(nums):
            if not small or num <= -small[0]:
                heapq.heappush(small, -num)
                sum_s += num; cnt_s += 1
            else:
                heapq.heappush(large, num)
                sum_l += num; cnt_l += 1
            balance()

            if i >= x:
                out = nums[i - x]
                del_map[out] += 1
                if out <= -small[0]:
                    cnt_s -= 1; sum_s -= out
                    if out == -small[0]: prune(small, True)
                else:
                    cnt_l -= 1; sum_l -= out
                    if large and out == large[0]: prune(large, False)
                balance()

            if i >= x - 1:
                med = -small[0]
                cost[i] = (med * cnt_s - sum_s) + (sum_l - med * cnt_l)

        # 2. DP: dp[i] stores min cost for choosing j windows in prefix nums[0..i]
        dp = [0] * n
        for j in range(1, k + 1):
            next_dp = [float('inf')] * n
            for i in range(x * j - 1, n):
                skip = next_dp[i - 1] if i > 0 else float('inf')
                # Base case: 0 windows cost 0 across any prefix length
                prev = 0 if j == 1 else (dp[i - x] if i - x >= 0 else float('inf'))
                next_dp[i] = min(skip, prev + cost[i])
            dp = next_dp

        return dp[n - 1]
