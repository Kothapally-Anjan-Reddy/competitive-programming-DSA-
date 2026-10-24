class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        swaps=0
        mapping={}
        def get_digit_sum(x):
            return sum(int(digit) for digit in str(x))

        sorted_nums=sorted(nums,key=lambda x: (get_digit_sum(x),x))
        for i,num in enumerate(nums):
            mapping[num]=i
        
        for i in range(len(nums)):
            if sorted_nums[i]!=nums[i]:
                expected_num=sorted_nums[i]
                expected_idx=mapping[expected_num]
                mapping[nums[i]],mapping[expected_num]=mapping[expected_num],mapping[nums[i]]
                nums[i],nums[expected_idx]=nums[expected_idx],nums[i]
                swaps+=1

        return swaps
