class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        rows,columns=len(grid),len(grid[0])
        directions=[[1,0],[0,1]]
        MOD=10**9+7

        dp=[[[0,0] for _ in range(columns)] for _ in range(rows)]
        dp[rows-1][columns-1][0]=1
        dp[rows-1][columns-1][1]=1  #This means if we reached the last cell from right then we have 1 way to reach the destination that is towards down

        for i in range(rows-1,-1,-1):
            for j in range(columns-1,-1,-1):
                if i==rows-1 and j==columns-1:
                    continue
                
                down_ways=dp[i+1][j][0] if i+1<rows else 0
                right_ways=dp[i][j+1][1] if j+1<columns else 0

                if grid[i][j]==0:
                    val=(down_ways+right_ways)%MOD
                    dp[i][j][0]=dp[i][j][1]=val
                else:
                    dp[i][j][0]=right_ways%MOD
                    dp[i][j][1]=down_ways%MOD
        
        return (dp[1][0][0] + dp[0][1][1]) % MOD
