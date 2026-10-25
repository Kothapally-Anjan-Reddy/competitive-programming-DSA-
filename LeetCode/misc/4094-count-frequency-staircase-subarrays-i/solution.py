class Solution:
    def countStaircase(self, nums: list[int]) -> int:
        res=0
        freq={}
        order=[]
        for i in range(len(nums)):
            freq.clear()
            order.clear()
            for j in range(i,len(nums)):
                num=nums[j]
                if num not in freq:
                    order.append(num)
                freq[num]=freq.get(num,0)+1
            
                stair=True
                for idx,num in enumerate(order):
                    if freq[num]!=idx+1:
                        stair=False
                        break
                if stair:
                    res+=1

        return res
