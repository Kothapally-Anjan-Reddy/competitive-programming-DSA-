class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        x=float('inf')
        y=float('inf')

        if len(ops)==0: return m*n

        for op in ops:
            x=min(x,op[0])
            y=min(y,op[1])
        
        if x!=0 and y!=0: return x*y
        elif x!=0 or y!=0: return max(x,y)
        else: return 1
