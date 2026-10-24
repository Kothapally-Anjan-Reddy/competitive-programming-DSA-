class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextgreater=[-1] * len(nums2)
        stack=[]
        results=[]
        dictionary={}

        for i,num in enumerate(nums2):            #Monotonic Decreasing stack
            if len(stack)!=0:
                while num>nums2[stack[-1]]:
                    nextgreater[stack[-1]]=num
                    stack.pop()
                    if len(stack)==0: break
            stack.append(i)
            dictionary.update({num:i})

        for i,num in enumerate(nums1):
            index=dictionary.get(num)
            results.append(nextgreater[index])

        return results
