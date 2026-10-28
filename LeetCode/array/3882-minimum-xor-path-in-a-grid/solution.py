class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        rows,columns=len(grid),len(grid[0])
        # dp=defaultdict(lambda: defaultdict(set))
        dp = [[set() for _ in range(columns)] for _ in range(rows)]
        dp[-1][-1].add(grid[-1][-1])

        for r in range(rows-1,-1,-1):
            for c in range(columns-1,-1,-1):
                val=grid[r][c]
                if r==rows-1 and c==columns-1:
                    dp[r][c].add(val)
                    continue
                if r<rows-1:
                    dp[r][c].update(val^x for x in dp[r+1][c])
                if c<columns-1:
                    dp[r][c].update(val^x for x in dp[r][c+1])
        
        return min(dp[0][0])
