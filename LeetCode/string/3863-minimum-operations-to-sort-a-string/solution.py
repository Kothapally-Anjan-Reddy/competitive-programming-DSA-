class Solution:
    def minOperations(self, s: str) -> int:
        target="".join(sorted(s))
        if s==target:
            return 0
        
        if len(s)<=2:
            return -1
        
        else:
            highest,lowest=0,0
            for i in range(len(s)):
                if s[i]>=s[highest]:
                    highest=i
                if s[i]<s[lowest]:
                    lowest=i
            
            if lowest==0 or highest==len(s)-1: return 1
            elif lowest==len(s)-1 and highest==0: return 3
            else: return 2
