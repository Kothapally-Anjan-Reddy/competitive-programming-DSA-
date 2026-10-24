class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        left=0
        right=0
        res=""

        for i in s:
            if i=='(':
                if left>0:
                    res+='('
                left+=1
            else:
                if left>1:
                    res+=')'
                left-=1
                
        return res
