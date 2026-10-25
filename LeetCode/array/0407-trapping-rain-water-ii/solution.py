import heapq
class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        q=[]
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        rows,columns=len(heightMap),len(heightMap[0])
        visited=set()

        for r in range(rows):
            for c in range(columns):
                if r==0 or c==0 or r==rows-1 or c==columns-1:
                    visited.add((r,c))
                    q.append((heightMap[r][c],r,c))
        heapq.heapify(q)

        maxi=-1
        water=0
        while q:
            h,row,col=heapq.heappop(q)
            maxi=max(h,maxi)
            water+=maxi-h
            for rn,cn in directions:
                r,c=row+rn,col+cn
                if r in range(rows) and c in range(columns) and (r,c) not in visited:
                    heapq.heappush(q,(heightMap[r][c],r,c))
                    visited.add((r,c))

        return water
