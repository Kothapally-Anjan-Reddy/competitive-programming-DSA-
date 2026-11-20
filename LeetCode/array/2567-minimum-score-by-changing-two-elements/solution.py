class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        if len(nums)<4:
            return 0
        nums.sort()
        return min(abs(nums[-1]-nums[2]),abs(nums[-3]-nums[0]),abs(nums[-2]-nums[1]))
