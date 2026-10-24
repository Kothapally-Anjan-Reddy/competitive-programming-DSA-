class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res=[]

        def dfs(visited,subset):
            if len(subset)==len(nums):
                res.append(subset.copy())
                return

            for num in nums:
                if num not in visited:
                    subset.append(num)
                    visited.add(num)
                    dfs(visited,subset)
                    subset.pop()
                    visited.remove(num)
            
        dfs(set(),[])
        return res
