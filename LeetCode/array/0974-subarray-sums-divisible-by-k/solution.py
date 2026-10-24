class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        hashe = {0: 1}
        total = 0

        for num in nums:
            total += num
            rem = total % k

            count += hashe.get(rem, 0)
            hashe[rem] = hashe.get(rem, 0) + 1

        return count
