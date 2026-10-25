class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        a1=bin(a)[2:]
        b1=bin(b)[2:]
        s1,s2=0,0
        for i in a1:
            if i=='1':
                s1+=1
        for i in b1:
            if i=='1':
                s2+=1
        return s1*s2 if s1>=s2 else int(s2/s1)
