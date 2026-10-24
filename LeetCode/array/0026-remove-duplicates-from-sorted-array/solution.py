class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # position=0
        # pre=None
        # for i in nums:
        #     if(i==pre):
        #         continue
        #     pre=i
        #     nums[position]=i
        #     position+=1
        
        # return position

        # with 2 pointers:

        left=0
        right=1

        while(right<len(nums)):
            if(nums[left]==nums[right]):
                right+=1
            else:
                left+=1
                nums[left]=nums[right]
                right+=1
    
        return left+1
