class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows,columns=len(grid),len(grid[0])
        islands=0
        visited=set()
        directions=[(0,1),(0,-1),(1,0),(-1,0)]

        def bfs(i,j):
            q=deque()
            q.append((i,j))
            closed=True
            while q:
                ros,cols=q.popleft()
                for row,col in directions:
                    r,c=ros+row,cols+col
                    if ((r,c) not in visited and r in range(rows) and c in range(columns) and grid[r][c]==0):
                        visited.add((r,c))
                        q.append((r,c))
                        if r==rows-1 or c==columns-1 or r==0 or c==0:
                            closed=False
                            
            return closed

        for i in range(1,rows-1):
            for j in range(1,columns-1):
                if  grid[i][j]==0 and (i,j) not in visited:
                    visited.add((i,j))
                    if bfs(i,j):
                        islands+=1
        
        return islands
