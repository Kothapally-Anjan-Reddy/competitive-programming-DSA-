class Solution:
    def trap(self, height: list[int]) -> int:
        max_right=[0]*len(height)
        h=0
        for i in range(len(height)-1,-1,-1):
            max_right[i]=h
            h=max(h,height[i])
        
        h=0
        water=0
        for i in range(len(height)):
            res=min(h,max_right[i])-height[i]
            if res>0:
                water+=res
            h=max(h,height[i])
        
        return water
