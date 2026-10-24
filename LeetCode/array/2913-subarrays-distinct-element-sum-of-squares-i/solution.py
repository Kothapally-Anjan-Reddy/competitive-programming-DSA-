class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        unique=set()
        res=0

        for i in range(len(nums)):
            unique.clear()
            for j in range(i,len(nums)):
                unique.add(nums[j])
                res+=len(unique)**2

        return res
