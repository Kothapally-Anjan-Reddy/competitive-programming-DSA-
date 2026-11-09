class Solution:
    from sortedcontainers import SortedList
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        li=[]
        for i in range(k):
            li.append(i)

        available=SortedList(li)
        busy=[]
        count=[0]*k

        for i in range(len(arrival)):
            x = i % k
            while busy and busy[0][0]<=arrival[i]:
                time,idx=heapq.heappop(busy)
                available.add(idx)
            
            if not available:
                continue

            pos = available.bisect_left(x)
            if pos==len(available):
                pos=0
            idx=available[pos]
            count[idx]+=1
            heapq.heappush(busy,(arrival[i] + load[i],idx))
            available.remove(idx)

        maxi=max(count)

        return [i for i,x in enumerate(count) if x == maxi]
