class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        res=float('inf')
        for i in range(0,len(nums),2):
            num=int(str(nums[i])+str(nums[i+1]))
            res=min(res,num)
        
        return res
