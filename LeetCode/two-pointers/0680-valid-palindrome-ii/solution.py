class Solution:
    def validPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        res=True
        
        def palindrome(left: int,right: int):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                res= (palindrome(left+1,right) or palindrome(left,right-1))
                break
        
        return res
