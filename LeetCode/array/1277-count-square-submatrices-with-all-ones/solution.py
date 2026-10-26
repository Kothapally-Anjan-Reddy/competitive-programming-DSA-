class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        rows,columns=len(matrix),len(matrix[0])
        dp=defaultdict(int)
        res=0
        
        for r in range(rows):
            for c in range(columns):
                if matrix[r][c]:
                    dp[(r,c)]=1+min(dp[r-1,c], dp[(r,c-1)], dp[(r-1,c-1)])
                    res+=dp[(r,c)]

        return res
