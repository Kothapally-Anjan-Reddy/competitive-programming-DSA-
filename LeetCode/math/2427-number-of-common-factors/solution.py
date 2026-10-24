class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        if a==1 or b==1: return 1
        x=min(a,b)
        counter=0
        for i in range(1,x+1):
            if a%i==0 and b%i==0:
                counter+=1
        
        return counter
