class Solution:
    def canAliceWin(self, n: int) -> bool:
        x=10
        alice=1
        while n>=0:
            if alice==1 and n-x<0:
                return False
            alice*=-1
            n-=x
            x-=1
        return True
