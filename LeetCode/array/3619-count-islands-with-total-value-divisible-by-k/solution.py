from collections import deque
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows,columns=len(grid), len(grid[0])
        visited=set()
        res=0
        directions=[[0,1],[0,-1],[1,0],[-1,0]]

        def bfs(r,c):
            q=deque()
            q.append((r,c))
            visited.add((r,c))
            total=grid[r][c]

            while q:
                row,col=q.popleft()
                for dr,dc in directions:
                    r,c=row+dr,col+dc
                    if (r in range(rows) and c in range(columns) and (r,c) not in visited and grid[r][c]!=0):
                        visited.add((r,c))
                        q.append((r,c))
                        total+=grid[r][c]
            return total % k==0


        for r in range(rows):
            for c in range(columns):
                if (r,c) not in visited and grid[r][c]!=0:
                    if bfs(r,c):
                        res+=1
        
        return res
