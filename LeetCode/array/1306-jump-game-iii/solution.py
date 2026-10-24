class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        visited=set()
        
        def dp(i):
            if arr[i]==0:
                return True
            visited.add(i)
            
            pre=i-arr[i]
            nxt=i+arr[i]
            if pre not in visited and pre in range(len(arr)) and dp(pre):
                return True

            if nxt not in visited and nxt in range(len(arr)) and dp(nxt):
                return True
            
            return False
        
        return dp(start)
