class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        maxi=float('-inf')

        while l<r:
            val=(r-l)*min(height[r],height[l])
            maxi=max(maxi,val)
            if height[r]>=height[l]:
                l+=1
            else:
                r-=1

        return maxi
