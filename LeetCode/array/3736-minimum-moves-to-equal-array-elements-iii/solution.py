class Solution:
    def minMoves(self, nums: List[int]) -> int:
        ref=max(nums)
        return sum(ref-num for num in nums)
