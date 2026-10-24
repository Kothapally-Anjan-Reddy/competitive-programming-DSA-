class Solution:
    def subarraySum(self,nums: list[int], k: int):

        hashe={}
        sum=0
        count=0
        
        # for i,num in enumerate(nums):
        #     sum+=num
        #     if sum==k:
        #         count+=1
                
        #     if sum-k in hashe:
        #         j=hashe.get(sum-k)
        #         count+=j
            
        #     if sum not in hashe:
        #         hashe.update({sum:1})
        #     else:
        #         j=hashe.get(sum)
        #         hashe.update({sum:j+1})

        # return count





































        for i,num in enumerate(nums):
            sum+=num          
            if sum==k:
                count+=1
            if sum-k in hashe:
                count+=hashe[sum-k]

            hashe[sum]=hashe.get(sum,0)+1

        return count
