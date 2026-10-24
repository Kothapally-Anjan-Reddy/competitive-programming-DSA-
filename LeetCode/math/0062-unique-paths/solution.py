class Solution:
    dic={}
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 or n==1:
            return 1
        else:
            if (m-1,n) not in self.dic:
                self.dic[(m-1,n)]=self.uniquePaths(m-1,n)
            if (m,n-1) not in self.dic:
                self.dic[(m,n-1)]=self.uniquePaths(m,n-1)
            k1=self.dic[(m-1,n)]
            k2=self.dic[(m,n-1)]
            return k1 + k2
