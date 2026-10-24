class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        nums.sort()
        count=1
        maxi=0
        prev=nums[0]
        for i,current in enumerate(nums[1:]):
            if current==prev+1:
                count+=1
            elif current==prev:
                continue
            else:
                maxi=max(maxi,count)
                count=1
            prev=current
        maxi=max(maxi,count)

        return maxi
