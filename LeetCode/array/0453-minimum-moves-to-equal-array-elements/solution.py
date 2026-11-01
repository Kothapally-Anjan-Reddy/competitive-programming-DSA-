class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mini=min(nums)
        return sum([x-mini for x in nums])
