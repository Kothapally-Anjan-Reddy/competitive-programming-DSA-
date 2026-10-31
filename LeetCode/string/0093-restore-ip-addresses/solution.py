class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        if len(s)>12 or len(s)<4:return []
        result=[]

        def backtrack(i,point,subset):
            if point==4 and i==len(s):
                result.append(subset[:-1])
                return
            
            elif point>4:
                return
            
            for j in range(i,min(i+3,len(s))):
                if int(s[i:j+1])<=255 and (i==j or s[i]!='0'):
                    backtrack(j+1,point+1, subset + s[i:j+1] +'.')

        backtrack(0,0,"")
        return result
