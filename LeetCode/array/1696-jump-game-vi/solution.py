from collections import deque
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            return nums[0]

        q=deque()
        q.append(len(nums)-1)
        dp=[None]*len(nums)
        dp[len(nums)-1]=nums[-1]

        for i in range(len(nums)-2,-1,-1):
            if q[0]>i+k:
                q.popleft()
            dp[i]=nums[i]+dp[q[0]]
            while q and dp[q[-1]]<dp[i]:
                q.pop()
            q.append(i)
        
        return dp[0]
