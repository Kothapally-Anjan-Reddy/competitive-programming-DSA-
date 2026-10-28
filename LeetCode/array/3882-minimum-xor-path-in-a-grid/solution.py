class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        res=float('inf')
        rows,columns=len(grid),len(grid[0])
        dp={}

        def dfs(r,c):
            if (r,c) in dp:
                return dp[(r,c)]

            if r==rows-1 and c==columns-1:
                return {grid[r][c]}
            
            res=set()
            if r<rows-1:
                for x in dfs(r+1,c):
                    res.add(x^grid[r][c])
            if c<columns-1:
                for x in dfs(r,c+1):
                    res.add(x^grid[r][c])
            
            dp[(r,c)]=res
            return res
            
        return min(dfs(0,0))
