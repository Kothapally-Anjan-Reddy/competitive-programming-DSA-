class Solution:
    def canTransform(self, source: list[int], target: list[int]) -> bool:
        # Solves 635/640 test cases
        # i=0
        # j=0
        # count=0
        # while i<len(source):
        #     if source[i]!=target[i]:
        #         if count>2:
        #             return False
        #         elif count==1:
        #             if source[i]+source[j]!=target[j]+target[i]:
        #                 return False
        #         elif count==0:
        #             j=i
        #         count+=1
        #     i+=1
        # return True if count!=1 else False

        return sum(source)==sum(target)
