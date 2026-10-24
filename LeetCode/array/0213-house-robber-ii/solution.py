import copy
class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums)<4:
            return max(nums)
        dp1=[-1]* (len(nums)+2)
        dp1[-1]=0
        dp1[-2]=0
        dp2=copy.deepcopy(dp1)

        def robber(i,j,dp):
            if i>=j:
                return 0
            
            if dp[i]!=-1:
                return dp[i]
            
            dp[i]=max(nums[i]+robber(i+2,j,dp),robber(i+1,j,dp))
            return dp[i]

        return max(robber(0,len(nums)-1,dp1),robber(1,len(nums),dp2))
