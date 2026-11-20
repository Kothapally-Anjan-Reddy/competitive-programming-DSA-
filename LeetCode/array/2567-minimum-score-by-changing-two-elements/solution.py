class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        # Instead of sorting just use the heap to find the first 3 smallest and last 3 smallest elements which are only required for the answer
        s1,s2,s3=heapq.nsmallest(3,nums)
        l1,l2,l3=heapq.nlargest(3,nums)

        return min(
            l1-s3,
            l3-s1,
            l2-s2
        )
