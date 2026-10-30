class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj=[[] for _ in range(n)]

        for s,d,w in edges:
            adj[s].append([d,w])
        
        shortest=set()
        heap=[(0,0,1)]

        while heap:
            w1,n1,c1=heapq.heappop(heap)
            if (n1,c1) in shortest:
                continue
            
            shortest.add((n1,c1))

            if n1==n-1:
                return w1
            
            for n2,w2 in adj[n1]:
                if labels[n1]==labels[n2]:
                    new_count=c1+1
                else:
                    new_count=1
            
                if new_count>k:
                    continue
                if (n2,new_count) not in shortest:
                    heapq.heappush(heap,(w1+w2,n2,new_count))

        return -1
