class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        freq = Counter(ranks)
        n = len(ranks)

        # Total combined speed factor S = sum(1 / sqrt(r))
        sum_inv_sqrt = sum(count / math.sqrt(r) for r, count in freq.items())

        # Tighter search bounds
        l = max(1, int((cars / sum_inv_sqrt) ** 2))
        r = min(
            min(ranks) * cars * cars,
            math.ceil(((cars + n) / sum_inv_sqrt) ** 2),
        )
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
