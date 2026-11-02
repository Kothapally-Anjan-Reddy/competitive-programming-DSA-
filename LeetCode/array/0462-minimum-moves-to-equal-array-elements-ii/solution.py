import numpy as np
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        array = np.partition(np.array(nums), len(nums) // 2)
        medium = int(array[len(array) // 2])

        return sum(abs(num-medium) for num in nums)
