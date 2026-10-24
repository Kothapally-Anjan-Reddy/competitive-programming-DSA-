class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited=set()
        islands=0
        rows,columns=len(grid),len(grid[0])
        directions=[[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(row,col):
            q=collections.deque()
            q.append((row,col))
            res=True

            while q:
                row,col=q.popleft()
                for dr,dc in directions:
                    r,c=row+dr,col+dc
                    if (r in range(rows) and
                    c in range(columns) and
                    grid[r][c]==0 and 
                    (r,c) not in visited):
                        visited.add((r,c))
                        q.append((r,c))
                        if (r==0 or r==rows-1 or c==0 or c==columns-1):
                            res=False
            return res

        for r in range(rows):
            for c in range(columns):
                if grid[r][c]==0 and (r,c) not in visited:
                    res=bfs(r,c)
                    visited.add((r,c))
                    if (r!=0 and r!=rows-1 and c!=0 and c!=columns-1 and res):
                        islands+=1

        return islands
