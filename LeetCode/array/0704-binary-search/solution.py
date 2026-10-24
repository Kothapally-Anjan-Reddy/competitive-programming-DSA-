class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(l,r):
            if l>r:
                return -1
            m=((l+r)//2)
            if nums[m]==target:
                return m
            elif nums[m]>target:
                return binary(l,m-1)
            else:
                return binary(m+1,r)
        res=binary(0,len(nums)-1)
        return res
