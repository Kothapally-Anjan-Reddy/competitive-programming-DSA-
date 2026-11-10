class Solution:
    def countValidSubstrings(self, s: str) -> int:
        l,count=0,0

        for r in range(len(s)):
            if r>1 and s[r-2:r+1]=="abc":
                l=r-1
            count+=r-l+1
        
        return count
