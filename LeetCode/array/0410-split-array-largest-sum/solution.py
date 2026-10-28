class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        l,r=max(nums),sum(nums)
        res=r

        def canSplit(largest):
            total=0
            subarrays=0
            for num in nums:
                total+=num
                if total>largest:
                    subarrays+=1
                    total=num
            return subarrays+1<=k

        while l<=r:
            mid=(l+r)//2
            if canSplit(mid):
                res=mid
                r=mid-1
            else:
                l=mid+1
        
        return res
