class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum=float('-inf')
        resl=1
        resr=1
        for i in range(len(nums)):
            resl*=nums[i]
            resr*=nums[len(nums)-i-1]

            maximum=max(maximum,resl,resr)
            if resl==0:
                resl=1
            if resr==0:
                resr=1

        return maximum
