from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap=Counter(tasks)
        maxHeap=[-x for x in maxHeap.values()]
        heapq.heapify(maxHeap)
        time=0
        q=deque() #this is for the pairs of (cnt,idle time) - is for max Heap

        while q or maxHeap:
            if maxHeap:
                cnt=1+heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt,time+n])
            
            if q and q[0][1]==time:
                heapq.heappush(maxHeap,q.popleft()[0])
            time+=1

        return time
