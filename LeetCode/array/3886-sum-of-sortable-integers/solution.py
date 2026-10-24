class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        divisors=[]
        n=len(nums)
        for i in range(1,n+1):
            if n%i==0:
                divisors.append(i)

        def check(nums1,nums2): #nums1 is checking array and num2 is the sorted array
            L=len(nums1)
            for i in range(L-1):
                if nums1[i]>nums1[i+1]:
                    return nums1[i+1:]+nums1[:i+1]==nums2
            return nums1==nums2
        
        target=sorted(nums)
        res=0
        for div in divisors:
            can_be_sorted=True
            for start in range(0,n,div):
                if not check(nums[start:start+div],target[start:start+div]):
                    can_be_sorted=False
                    break

            if can_be_sorted:
                res+=div
        
        return res
