class Solution:
    def trap(self, arr: List[int]) -> int:
        if len(arr)<3:
            return 0
        l=0
        water=0
        while arr[l] and arr[l]==0:
            l+=1
        middle=0
        r=l+1
        while r<len(arr):
            if arr[r]<arr[l]:
                middle+=arr[r]
                r+=1
            else:
                val=min(arr[r],arr[l])
                water+=val*(r-l-1)-middle
                middle=0
                l=r
                r+=1
        left=l
        r=len(arr)-1
        l=r-1
        middle=0
        while l>=left:
            if arr[l]<arr[r]:
                middle+=arr[l]
                l-=1
            else:
                val=min(arr[r],arr[l])
                water+=val*(abs(r-l)-1)-middle
                middle=0
                r=l
                l-=1
        return water
