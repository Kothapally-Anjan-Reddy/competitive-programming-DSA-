class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        l,r=1,min(ranks)*cars*cars
        res=r

        while l<=r:
            mid=l+((r-l)//2)
            done=0
            for rank in ranks:
                val=isqrt(mid//rank)
                done+=val
            
            if done>=cars:
                res=min(res,mid)
                r=mid-1
            else:
                l=mid+1
        
        return res
