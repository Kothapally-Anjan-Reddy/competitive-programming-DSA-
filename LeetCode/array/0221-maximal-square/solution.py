class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        res=0
        dp=defaultdict(int)
        rows,columns=len(matrix),len(matrix[0])
        maxi=0

        for r in range(rows):
            for c in range(columns):
                if matrix[r][c]=='1':
                    dp[(r,c)]=1+min(dp[(r-1,c)], dp[(r,c-1)], dp[(r-1,c-1)])
                    maxi=max(maxi,dp[(r,c)])

        
        return maxi*maxi
