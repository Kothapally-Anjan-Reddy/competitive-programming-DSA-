class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        result=0
        res=0
        for i in range(len(nums)):
            if nums[i]>=minK and nums[i]<=maxK:
                res+=1
            else:
                result+=(res*(res+1))//2
                res=0
        result+=(res*(res+1))//2
        return result
