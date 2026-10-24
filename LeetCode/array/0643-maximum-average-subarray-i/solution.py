class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumi=0
        left=0
        right=0
        maxi=sumi

        while(right<len(nums)):
            if(right<k):
                sumi+=nums[right]
                maxi=sumi
                right+=1
            else:
                sumi-=nums[left]
                left+=1
                sumi+=nums[right]
                right+=1
                if(sumi>maxi):
                    maxi=sumi

        return maxi/k
