class Solution:
    def checkValidString(self, s: str) -> bool:
        can_be_close=0
        can_be_open=0
        for i in range(len(s)):
            if s[i]==')':
                if can_be_close==0:return False
                can_be_close-=1
            else:
                can_be_close+=1
            if s[len(s)-1-i]=='(':
                if can_be_open==0:return False
                can_be_open-=1
            else:
                can_be_open+=1
        return True
