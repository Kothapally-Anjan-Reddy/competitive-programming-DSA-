class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        required = nums[len(nums) // 2]
        res=0

        for num in nums:
            res+=abs(num-required)
        
        return res
