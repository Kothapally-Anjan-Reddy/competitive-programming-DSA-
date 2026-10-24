class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        rows,columns=len(grid),len(grid[0])
        visited=set()
        maxfishes=0      # It counts the max fishes fisher can catch optimally
        water=0           # Counts number of water cells
        movements=[[0,1],[0,-1],[1,0],[-1,0]]

        def bfs(r,c):
            que=collections.deque()
            que.append((r,c))
            fish=grid[r][c]
            while que:
                row,col=que.popleft()
                for dr,dc in movements:
                    r,c=row+dr,col+dc
                    if (r in range(rows) and 
                       c in range(columns) and
                       (r,c) not in visited and
                       grid[r][c]!=0):
                       visited.add((r,c))
                       que.append((r,c))
                       fish+=grid[r][c]
            return fish

        for r in range(rows):
            for c in range(columns):
                if grid[r][c]!=0 and (r,c) not in visited:
                    visited.add((r,c))
                    fish=bfs(r,c)
                    maxfishes=max(maxfishes,fish)
                    water+=1

        return maxfishes
