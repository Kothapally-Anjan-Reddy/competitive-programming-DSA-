class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited=set()
        sub_islands=0
        rows,columns=len(grid2),len(grid2[0])
        directions=[[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(row,col):
            q=collections.deque()
            q.append((row,col))
            visited.add((row,col))
            res=True
            while q:
                row,col=q.popleft()
                if res==True and grid1[row][col]==0:
                    res=False

                for dr,dc in directions:
                    r,c=row+dr,col+dc
                    if (r in range(rows) and
                    c in range(columns) and
                    grid2[r][c]==1 and 
                    (r,c) not in visited):
                        visited.add((r,c))
                        q.append((r,c))
            return res

        for r in range(rows):
            for c in range(columns):
                if grid2[r][c]==1 and (r,c) not in visited:
                    res=bfs(r,c)
                    if res:
                        sub_islands+=1

        return sub_islands
