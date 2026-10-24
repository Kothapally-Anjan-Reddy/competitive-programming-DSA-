class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums=[num*num for num in nums]
        nums.sort(reverse=True)

        n=math.ceil(len(nums)/2)
        res=0
        for i in range(len(nums)):
            if i<n:
                res+=nums[i]
            else:
                res-=nums[i]
        
        return res
