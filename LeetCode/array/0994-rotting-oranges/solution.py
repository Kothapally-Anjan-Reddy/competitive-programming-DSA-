class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time,fresh=0,0
        rows,cols=len(grid),len(grid[0])
        directions=[[-1,0],[1,0],[0,-1],[0,1]]

        q=collections.deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    fresh+=1
                if grid[row][col]==2:
                    q.append((row,col))

        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    row,col=r+dr,c+dc

                    if (row in range(rows) and
                        col in range(cols) and
                        grid[row][col]==1):
                        grid[row][col]=2
                        q.append((row,col))
                        fresh-=1
            time+=1

        return time if fresh==0 else -1
