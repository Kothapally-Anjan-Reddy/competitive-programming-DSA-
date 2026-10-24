class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dict1={}

        # for i,num in enumerate(nums):
        #     if num not in dict1:
        #         dict1.update({num:i})
        #     else:
        #         if(i-dict1[num]<=k):
        #             return True
        #         else:
        #             dict1[num]=i

        # return False


        left=0
        right=0


        for i in range(0,min(len(nums),k)):
            if nums[right] in dict1:
                return True
            dict1.update({nums[right]:right})
            right+=1


        while(right<len(nums)):
            if nums[right] not in dict1:
                dict1.update({nums[right]:right})
                del dict1[nums[left]]
            else:
                return True
            left+=1
            right+=1

        return False
