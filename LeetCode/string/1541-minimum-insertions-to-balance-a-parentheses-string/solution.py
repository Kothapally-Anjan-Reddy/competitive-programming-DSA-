class Solution:
    def minInsertions(self, s: str) -> int:
        left,idx,res=0,0,0
        i=0
        while i<len(s):
            if s[i]=='(':
                left+=1
                i+=1
            else:
                if left>0:
                    left-=1
                else:
                    res+=1
                if i+1<len(s) and s[i+1]==')':
                    i+=2
                else:
                    i+=1
                    res+=1
        
        return res+(left*2)
