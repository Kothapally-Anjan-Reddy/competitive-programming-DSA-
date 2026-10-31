class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        MOD = 10**9 + 7

        dp = [[[0, 0] for _ in range(columns)] for _ in range(rows)]
        # Reaching target counts as 1 path for both arrival directions
        dp[rows - 1][columns - 1][0] = 1
        dp[rows - 1][columns - 1][1] = 1

        for i in range(rows - 1, -1, -1):
            for j in range(columns - 1, -1, -1):
                if i==rows-1 and j==columns-1:
                    continue

                down_ways = dp[i + 1][j][0] if i + 1 < rows else 0
                right_ways = dp[i][j + 1][1] if j + 1 < columns else 0

                if grid[i][j] == 0:
                    # Can move both down or right
                    dp[i][j][0] = (down_ways + right_ways) % MOD
                    dp[i][j][1] = (down_ways + right_ways) % MOD
                else:
                    # Must turn: came down -> must go right; came right -> must go down
                    dp[i][j][0] = right_ways
                    dp[i][j][1] = down_ways

        # At (0, 0), we can leave by going down (dp[1][0][0]) or right (dp[0][1][1])
        return (dp[1][0][0] + dp[0][1][1]) % MOD
