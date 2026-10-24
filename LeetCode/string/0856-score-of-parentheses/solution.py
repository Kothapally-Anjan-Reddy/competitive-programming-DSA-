class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        score=0

        for i in s:
            if i=='(':
                stack.append(-1)
            else:
                score=0
                while stack[-1]!=-1:
                    score+=stack.pop()
                
                if score==0:
                    stack[-1]=1
                else:
                    stack[-1]=2*score
        
        return sum(stack)
