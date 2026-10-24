class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        chardict={}
        for i in nums:
            if(i in chardict):
                return True
            else:
                chardict.update({i:1})
        return False
