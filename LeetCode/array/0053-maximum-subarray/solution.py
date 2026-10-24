class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total,maxi=0,float('-inf')
    
        for i in range(len(nums)):
            total+=nums[i]
            if total>maxi: maxi=total
            if total<0: total=0
        return maxi
