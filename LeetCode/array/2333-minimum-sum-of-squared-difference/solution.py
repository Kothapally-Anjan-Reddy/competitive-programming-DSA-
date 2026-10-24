class Solution:
    import heapq
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff={}
        res=0
        k=k1+k2
        total=0
        for i in range(len(nums1)):
            num=abs(nums1[i]-nums2[i])
            total+=num
            diff[num]=diff.get(num,0)+1

        if total<=k: return 0
        
        heap=[(-val,freq) for val,freq in diff.items()]
        heapq.heapify(heap)
        while k>0:
            if heap[0][0]==0 or heap[0][1]>k: break
            val,freq = heapq.heappop(heap)
            k-=freq
            if heap and heap[0][0]==val+1:
                _,f=heapq.heappop(heap)
                freq+=f
            heapq.heappush(heap,(val+1,freq))

        heap.sort()

        for val,freq in heap:
            less=val+1
            while freq>0:
                if k>0:
                    res+=less*less
                    k-=1
                else:res+=val*val
                freq-=1
                
        return res
