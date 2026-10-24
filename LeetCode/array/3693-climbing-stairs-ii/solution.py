class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        if n==0:
            return 0
        if n==1:
            return costs[0]+1
            
        mincost=[-1]*len(costs)

        def cost(n):
            if n<0:
                return float('inf')
            if n==0:
                return 0
            else:
                if mincost[n-1]==-1:
                    mincost[n-1]=cost(n-1)
                if mincost[n-2]==-1:
                    mincost[n-2]=cost(n-2)
                if mincost[n-3]==-1:
                    mincost[n-3]=cost(n-3)
            
                a=mincost[n-1]
                b=mincost[n-2]
                c=mincost[n-3]

                return costs[n-1]+min(a+1,b+4,c+9)
                
        return cost(n)


        # This works but results in tle, i.e using direct fibanocci without DP
