class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rows,columns=len(grid),len(grid[0])
        row,col=[0]*rows, [0]*columns
        res=0

        for r in range(rows):
            for c in range(columns):
                if grid[r][c]==1:
                    row[r]+=1
                    col[c]+=1
        for r in range(rows):
            for c in range(columns):
                if grid[r][c]==1 and (row[r]>1 or col[c]>1):
                    res+=1
        
        return res
