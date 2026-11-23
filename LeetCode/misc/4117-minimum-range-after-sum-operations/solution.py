class Solution:
    def minRange(self, a: int, b: int, c: int) -> int:
        a,b,c=sorted((a,b,c),reverse=True)
        return min(a-c,b)
