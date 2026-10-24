class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        res=0
        idx=0

        for i in range(len(nums)):
            if nums[i]<target:
                idx+=1
            elif nums[i]==target:
                res+=1
        
        result=[x for x in range(idx,idx+res)]

        return result
