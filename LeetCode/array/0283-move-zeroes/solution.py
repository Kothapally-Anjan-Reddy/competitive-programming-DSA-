class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # i=0
        # while(i<len(nums)):
        #     if(nums[i]==0):
        #         nums.pop(i)
        #         nums.append(0)
        #         continue
        #     i+=1                           should not be used as it pop takes O(n) complexity

        position=0

        for i,num in enumerate(nums):
            if(nums[i]!=0):
                nums[position]=nums[i]
                position+=1
            
        while(position<len(nums)):
            nums[position]=0
            position+=1
