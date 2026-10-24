class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows,columns=len(grid),len(grid[0])
        peri=0

        for r in range(rows):
            for c in range(columns):
                if grid[r][c]==1:
                    peri+=4
                    if (r-1 in range(rows) and grid[r-1][c]==1):
                        peri-=2
                    if (c-1 in range(columns) and grid[r][c-1]==1):
                        peri-=2
        
        return peri
