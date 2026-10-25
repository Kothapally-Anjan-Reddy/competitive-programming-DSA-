class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        rows,columns=len(matrix),len(matrix[0])
        visited={}
        res=0

        def dfs(r,c):
            if r not in range(rows) or c not in range(columns) or matrix[r][c]==0:
                return 0
            
            if (r,c) in visited:
                return visited[(r,c)]

            right=dfs(r+1,c)
            down=dfs(r,c+1)
            diag=dfs(r+1,c+1)
            visited[(r,c)]=min(right,down,diag)+1

            return visited[(r,c)]
        
        for row in range(rows):
            for col in range(columns):
                res+=dfs(row,col)

        return res
