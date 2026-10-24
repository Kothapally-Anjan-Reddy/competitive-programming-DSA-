class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color: return image
        stcolor=image[sr][sc]
        rows,columns=len(image),len(image[0])
        visited=set()
        directions=[[0,1],[0,-1],[1,0],[-1,0]]

        def bfs(r,c):
            que=collections.deque()
            visited.add((r,c))
            que.append((r,c))

            while que:
                row,col=que.popleft()

                for dr,dc in directions:
                    r,c=row+dr,col+dc
                    if ((r,c) not in visited and
                       r in range(rows) and
                       c in range(columns) and
                       image[r][c]==stcolor):
                       visited.add((r,c))
                       que.append((r,c))
                       image[r][c]=color

        
        image[sr][sc]=color
        bfs(sr,sc)

        return image
