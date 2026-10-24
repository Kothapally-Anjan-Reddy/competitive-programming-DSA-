class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
 
        final=0
        count=[0]*32

        for i in range(len(nums)):
            for j in range(32):
                if (nums[i] & 1<<j):
                    count[j]+=1


        while k>0:
            res=0
            for i in range(32):
                if count[i]>0:
                    count[i]-=1
                    res=res | 1<<i
            final+=(res*res)
                    
            k-=1

        return final % (pow(10,9)+7)
