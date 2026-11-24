class Solution:
    def maxLength(self, nums: List[int]) -> int:
        prod=1
        left=0
        length=2

        for right,num in enumerate(nums):
            while gcd(prod,num)>1:
                prod//=nums[left]
                left+=1
            prod*=num
            length=max(length,right-left+1)
        
        return length
