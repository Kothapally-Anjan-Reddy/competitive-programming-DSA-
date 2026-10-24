class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary={}

        for i,num in enumerate(nums):
            if target-num in dictionary:
                return [i,dictionary.get(target-num)]
            dictionary.update({num:i})
