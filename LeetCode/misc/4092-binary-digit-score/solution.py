class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        s1,s2=0,0
        for i in bin(a)[2:]:
            if i=='1':
                s1+=1
        for i in bin(b)[2:]:
            if i=='1':
                s2+=1
        return s1*s2 if s1>=s2 else int(s2/s1)
