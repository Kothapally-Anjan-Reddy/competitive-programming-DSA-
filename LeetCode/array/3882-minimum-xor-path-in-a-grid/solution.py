class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        rows,columns=len(grid),len(grid[0])
        dp=defaultdict(lambda: defaultdict(set))

        for r in range(rows-1,-1,-1):
            for c in range(columns-1,-1,-1):
                if r==rows-1 and c==columns-1:
                    dp[r][c].add(grid[r][c])
                    continue
                for x in dp[r+1][c]:
                    dp[r][c].add(grid[r][c]^x)
                for x in dp[r][c+1]:
                    dp[r][c].add(grid[r][c]^x)
        
        return min(dp[0][0])
