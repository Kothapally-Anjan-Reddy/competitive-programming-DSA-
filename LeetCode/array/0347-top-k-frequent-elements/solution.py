class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_frequency={}

        for num in nums:
            num_to_frequency[num]=num_to_frequency.get(num,0)+1

        li=sorted(num_to_frequency.items(),key=lambda x:x[1],reverse=True)

        return [x[0] for x in li[:k]]
