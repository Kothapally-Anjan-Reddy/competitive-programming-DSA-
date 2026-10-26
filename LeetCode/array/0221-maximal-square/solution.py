class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        res=0
        visited={}
        rows,columns=len(matrix),len(matrix[0])

        def dfs(r,c):
            if r not in range(rows) or c not in range(columns) or matrix[r][c]=="0":
                return 0
            
            if (r,c) in visited:
                return visited[(r,c)]
            
            visited[(r,c)]=1+min(dfs(r+1,c), dfs(r,c+1), dfs(r+1,c+1))
            return visited[(r,c)]

        for r in range(rows):
            for c in range(columns):
                res=max(res,dfs(r,c))
        
        return res*res
