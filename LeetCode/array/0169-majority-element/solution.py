class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency={}
        for num in nums:
            frequency[num]=frequency.get(num,0) + 1

        li=list(sorted(frequency.items(),key=lambda x:x[1],reverse=True))
        return li[0][0]

        # nums.sort()
        # count=0
        # maxi=0
        # prev=nums[0]
        # n=0

        # for num in nums:
        #     if num==prev:
        #         count+=1
        #     else:
        #         count=1
                
        #     if count>maxi:
        #         maxi=count
        #         n=num
            
        #     prev=num

        # return n
