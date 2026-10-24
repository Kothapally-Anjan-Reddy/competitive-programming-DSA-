class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        res=[]

        def dfs(i):
            if i==len(s):
                result.append(res.copy())
                return
            
            for j in range(i,len(s)):
                if self.ispalin(s,i,j):
                    res.append(s[i:j+1])
                    dfs(j+1)
                    res.pop()
        dfs(0)
        return result

    def ispalin(self,s,l,r):
        while r>l:
            if s[r]!=s[l]:
                return False
            l,r=l+1,r-1
        return True
