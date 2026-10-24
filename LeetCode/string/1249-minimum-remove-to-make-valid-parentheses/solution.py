class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        cnt=0
        res=""
        for i in range(len(s)):
            if s[i]=='(':
                cnt+=1
                res+=s[i]
            elif s[i]==')':
                if cnt>0:
                    res+=s[i]
                    cnt-=1
            else:
                res+=s[i]
        result=""
        print(res)

        for i in range(len(res)-1,-1,-1):
            if res[i]=='(' and cnt>0:
                cnt-=1
            else:
                result=res[i]+result
        return result
