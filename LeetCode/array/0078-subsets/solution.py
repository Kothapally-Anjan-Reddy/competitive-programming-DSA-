class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        subset=[]

        def dfs(index):     # Always write the nested functions inside the original one instead of outside because we do not have to send the parameters.
            if index>=len(nums):
                result.append(subset.copy())     #Always use the .copy() when we are using something which can be changed overtime like in backtracking.
                return

            subset.append(nums[index])
            dfs(index+1)

            subset.pop()
            dfs(index+1)

        dfs(0)

        return result
