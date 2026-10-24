class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        res=-1

        for i in range(len(nums)):
            if nums[i]!=i:
                if res==-1:
                    res=i
                else:
                    res=res & i
        return max(res,0)
