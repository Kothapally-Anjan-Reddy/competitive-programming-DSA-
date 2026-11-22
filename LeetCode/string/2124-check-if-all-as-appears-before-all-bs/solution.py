class Solution:
    def checkString(self, s: str) -> bool:
        b=0
        for chr in s:
            if chr=='a' and b!=0:
                return False
            elif chr=='b':
                b+=1
        return True
