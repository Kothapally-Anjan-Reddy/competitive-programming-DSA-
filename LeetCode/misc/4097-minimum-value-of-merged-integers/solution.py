class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        res=float('inf')
        n=len(nums)
        for i in range(0,n,2):
            num=int(str(nums[i])+str(nums[i+1]))
            res=min(res,num)
        
        return res
