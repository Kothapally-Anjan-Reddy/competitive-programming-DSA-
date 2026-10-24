class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,columns=len(grid),len(grid[0])
        visited=set()
        max_area=0
        directions=[[0,1],[0,-1],[1,0],[-1,0]]

        def bfs(row,col):
            q=collections.deque()
            q.append((row,col))
            visited.add((row,col))
            area=0

            while q:
                row,col=q.popleft()
                area+=1
                for dr,dc in directions:
                    r,c=row+dr,col+dc
                    if (r in range(rows) and
                    c in range(columns) and
                    grid[r][c]==1 and
                    (r,c) not in visited):
                        visited.add((r,c))
                        q.append((r,c))

            return area

        for r in range(rows):
            for c in range(columns):
                if grid[r][c]==1 and (r,c) not in visited:
                    area=bfs(r,c)
                    max_area=max(max_area,area)
        return max_area
