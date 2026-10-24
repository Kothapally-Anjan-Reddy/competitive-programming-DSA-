class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=set()
        islands=0
        rows,columns=len(grid),len(grid[0])
        directions=[[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(row,col):
            q=collections.deque()
            q.append((row,col))

            while q:
                row,col=q.popleft()
                for dr,dc in directions:
                    r,c=row+dr,col+dc
                    if (r in range(rows) and
                    c in range(columns) and
                    grid[r][c]=='1' and 
                    (r,c) not in visited):
                        visited.add((r,c))
                        q.append((r,c))

        for r in range(rows):
            for c in range(columns):
                if grid[r][c]=='1' and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1
                    visited.add((r,c))

        return islands
