class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s)<2:
            return 0
        
        stack=[]
        count=0

        for i in s:
            if i=='(':
                stack.append(i)
            else:
                score=0
                while stack and isinstance(stack[-1],int):
                    score+=stack.pop()
                if stack and stack[-1]=='(':
                    score+=2
                    stack.pop()
                    while stack and isinstance(stack[-1],int):
                        score+=stack.pop()
                    stack.append(score)
                else:
                    if score>0:
                        stack.append(score)
                    stack.append(i)
        
        for i in stack:
            if isinstance(i,int):
                count=max(i,count)

        return count
