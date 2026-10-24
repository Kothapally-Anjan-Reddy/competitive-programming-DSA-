class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # can_be_open,can_be_close=0,0

        # for i in s:
        #     if i=='(':
        #         can_be_close+=1
        #     else:
        #         if can_be_close==0:
        #             can_be_open+=1
        #         else:
        #             can_be_close-=1

        # return can_be_close + can_be_open

        stack=[]

        for i in s:
            if i=='(':
                stack.append(i)
            else:
                if stack and stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(i)

        return len(stack)
