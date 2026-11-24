class Solution:
    def maxLength(self, nums: List[int]) -> int:
        length=0
        for i in range(len(nums)-1):
            for j in range(i,len(nums)):
                arr=nums[i:j+1]
                if math.prod(arr) == (math.lcm(*arr) * math.gcd(*arr)):
                    length=max(length,j-i+1)
        return length
