class Solution:
    def minOperations(self, nums: list[int], locked: list[int], k: int) -> int:
        unlock=0
        reached=0
        for i in range(1,len(nums)+1):
            if i!=nums[i-1]:
                if nums[i-1]>i and reached<nums[i-1]:
                    for j in range(max(reached,i),nums[i-1]+1):
                        if locked[j-1]==1:
                            locked[j-1]=0
                            unlock+=1
                    reached=nums[i-1]
        
        if unlock>k:return -1
        swaps=0
        for i in range(len(nums)-1,0,-1):
            for j in range(i):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                    swaps+=1

        print(unlock,swaps)
        return swaps+unlock
