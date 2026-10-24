class Solution:
    def reverseVowels(self, s: str) -> str:
        left=0
        vowels=set("aeiouAEIOU")
        s=list(s)
        right=len(s)-1

        while right>left:
            while right>left and s[right] not in vowels:
                right-=1
            while right>left and s[left] not in vowels:
                left+=1

            s[left],s[right]=s[right],s[left]

            right-=1
            left+=1
        return "".join(s)
