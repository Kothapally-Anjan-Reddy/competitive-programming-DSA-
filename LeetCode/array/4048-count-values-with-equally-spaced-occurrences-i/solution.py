class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        dicti={}
        count=0
        for i,n in enumerate(nums):
            dicti.setdefault(n,[]).append(i)
            
        for key,vals in dicti.items():
            if len(vals)==3 and vals[2]-vals[1]==vals[1]-vals[0]:
                count+=1

        return count
