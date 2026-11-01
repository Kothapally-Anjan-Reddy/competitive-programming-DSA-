class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mini=min(nums)
        res=0
        for num in nums:
            res+=num-mini
        return res
