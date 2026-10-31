class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        res=0
        rows,columns=len(grid),len(grid[0])
        directions=[[0,1],[1,0]]
        dp={}
        
        def traverse(r,c,m):    # Row, column and the movement(0 for downa and 1 for right) from which it came
            if r==rows-1 and c==columns-1:
                return 1
            
            if (r,c,m) in dp:
                return dp[(r,c,m)]
            count=0
            if grid[r][c]==0:
                for dr,dc in directions:
                    row,col=r+dr,c+dc
                    if (row in range(rows) and col in range(columns)):
                        count= (count+traverse(row,col,abs(col-c))) % (10**9+7)
            else:
                if m==0:
                    row,col=r,c+1
                else:
                    row,col=r+1,c
                if (row in range(rows) and col in range(columns)):
                    count+=traverse(row,col,1-m)
            
            dp[(r,c,m)]=count
            return count
        
        return traverse(0,0,0)
