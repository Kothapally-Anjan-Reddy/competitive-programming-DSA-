class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        res=0
        arr=[]
        id={}
        for num in nums:
            val=int("".join(sorted(str(num),reverse=True)))
            arr.append((val-num))
        arr.sort(reverse=True)
        for dup in arr:
            if k>0:
                k-=1
                res+=dup
        return res+sum(nums)
