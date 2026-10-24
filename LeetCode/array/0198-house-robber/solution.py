class Solution:
    def rob(self, nums: list[int]) -> int:
        total=0
        dp=[-1]*(len(nums)+2)
        dp[0],dp[1]=0,0

        def robber(i):
            if i<2:
                return 0
            if dp[i]!=-1:
                return dp[i]

            dp[i]=max(nums[i-2]+robber(i-2),robber(i-1))
            return dp[i]
        
        return robber(len(nums)+1)
