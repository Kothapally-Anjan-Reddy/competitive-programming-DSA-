class MedianFinder:

    def __init__(self):
        self.small=[] # keep max heap to get last element
        self.large=[] # keep min heap to get the first element

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-num)
        heapq.heappush(self.large,-heapq.heappop(self.small))

        if len(self.large)-len(self.small)>1:
            heapq.heappush(self.small,-heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.large)>len(self.small):
            return self.large[0]
        else:
            return (-self.small[0]+self.large[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
