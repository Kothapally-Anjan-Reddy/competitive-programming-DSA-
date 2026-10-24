class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot=0
        prefix=[0]*(len(nums)+1)
        for i in range(len(nums)-1,-1,-1):
                prefix[i]=prefix[i+1]+nums[i]
            
        leftsum=0
        while pivot<len(nums):
            if prefix[pivot+1]==leftsum:
                return pivot
            leftsum+=nums[pivot]
            pivot+=1
        return -1
