class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow1(x,n):
            if x==0:
                return 0
            elif n==0:
                return 1
            
            res=pow1(x,n//2)
            res=res*res
            return res if n%2==0 else res*x
        
        res=pow1(x,abs(n))
        return res if n>=0 else 1/res
