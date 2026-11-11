class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        cost=0
        needs_min=min(need1,need2)

        cost=needs_min*min(costBoth,cost1+cost2)
        need1-=needs_min
        need2-=needs_min
        
        cost+=need1*min(costBoth,cost1)
        cost+=need2*min(costBoth,cost2)
        
        return cost
