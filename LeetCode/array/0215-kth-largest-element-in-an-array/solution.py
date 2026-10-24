class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        k=len(nums)-k+1

        heapq.heapify(nums)

        for i in range(0, k-1):
            heapq.heappop(nums)

        return nums[0]

        # return heapq.nlargest(k,nums)[-1]
