class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        mini=float('inf')

        for size in range(l,r+1):
            i,j=0,0
            total=0
            while j<len(nums):
                if j-i+1>size:
                    total-=nums[i]
                    i+=1
                total+=nums[j]
                if j-i+1==size and total>0: mini=min(total,mini)
                j+=1
        
        return mini if mini!=float('inf') else -1
