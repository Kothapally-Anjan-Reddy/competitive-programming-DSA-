class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num=set()
        for i in nums:
            num.add(i)
        
        i=1
        while True:
            if i not in num:
                return i
            i+=1
