class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp={}

        def decision(i,total):
            if i==len(nums):
                return 1 if total==target else 0
            
            if (i,total) in dp:
                return dp[(i,total)]

            dp[(i,total)]=(decision(i+1,total+nums[i]) +
                        decision(i+1,total-nums[i]))
            
            return dp[(i,total)]
        
        return decision(0,0)
