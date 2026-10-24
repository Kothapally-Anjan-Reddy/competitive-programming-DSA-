class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        s=str(x)
        r=s[::-1]
        return s==r
