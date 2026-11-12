class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longest,inc,dec=1,1,1

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                inc+=1
            else:
                inc=1
            if nums[len(nums)-i-1]>nums[len(nums)-i]:
                dec+=1
            else:
                dec=1
            longest=max(longest,inc,dec)
        
        return longest
