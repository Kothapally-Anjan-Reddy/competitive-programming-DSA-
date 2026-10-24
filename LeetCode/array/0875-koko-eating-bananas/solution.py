import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        while l<=r:
            m=(l+r)//2
            count=0
            for i in piles:
                count+=math.ceil(i/m)
            if count<=h:
                r=m-1
            else:
                l=m+1

        return l
