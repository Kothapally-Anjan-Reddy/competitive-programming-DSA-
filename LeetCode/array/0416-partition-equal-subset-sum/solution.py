class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumi=sum(nums)
        if sumi%2!=0:
            return False
        
        total=sumi//2
        
        dp=set()
        dp.add(0)

        for i in range(len(nums)-1,-1,-1):
            new_dp=set()
            for t in dp:
                if t+nums[i] == total:
                    return True
                new_dp.add(t+nums[i])
                new_dp.add(t)
            dp=new_dp
        
        return True if total in dp else False
