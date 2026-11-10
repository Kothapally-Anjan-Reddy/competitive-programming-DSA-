class Solution:
    def countValidSubstrings(self, s: str) -> int:
        a,b,c=-1,-1,-1
        count=0

        for i,ch in enumerate(s):
            if ch=='a':
                a=i
            elif ch=='b':
                b=a
            else:
                c=b
            count+=i-c

        return count
