class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        dicti={}
        count=0
        for i,n in enumerate(nums):
            dicti.setdefault(n,[]).append(i)
            
        for key,vals in dicti.items():
            if len(vals)>=3:
                diff=vals[1]-vals[0]
                prev=vals[1]
                ans=True
                for val in vals[2:]:
                    if val-prev!=diff:
                        ans=False
                    prev=val
                if ans:
                    count+=1

        return count
