class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Quick check for length 1
        counts_1 = Counter(nums)
        if any(v == 1 for v in counts_1.values()):
            return 1

        MOD1, BASE1 = 10**9 + 7, 1315423911
        MOD2, BASE2 = 10**9 + 9, 2654435761

        p1, p2 = [1] * (n + 1), [1] * (n + 1)
        h1, h2 = [0] * (n + 1), [0] * (n + 1)

        for i, val in enumerate(nums):
            p1[i + 1] = (p1[i] * BASE1) % MOD1
            p2[i + 1] = (p2[i] * BASE2) % MOD2
            h1[i + 1] = (h1[i] * BASE1 + val) % MOD1
            h2[i + 1] = (h2[i] * BASE2 + val) % MOD2

        def has_unique(length: int) -> bool:
            seen = Counter()
            for i in range(n - length + 1):
                sub1 = (h1[i + length] - h1[i] * p1[length]) % MOD1
                sub2 = (h2[i + length] - h2[i] * p2[length]) % MOD2
                seen[(sub1 << 32) | sub2] += 1
            return any(c == 1 for c in seen.values())

        low, high, ans = 2, n, n
        while low <= high:
            mid = (low + high) // 2
            if has_unique(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
