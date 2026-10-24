class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=""
        ori=""
        for i in s:
            if i.isalpha() or i.isnumeric():
                ori=ori+i.lower()
        for i in ori:
            string=i+string
        if(string==ori):
            return True
        else:
            return False


        left=0
        right=len(s)-1

        while(left<right):
            if(not s[left].isalpha() or not s[left].isnumeric()):
                left+=1
                continue
            if(not s[right].isalpha() or not s[right].isnumeric()):
                right-=1
                continue
            if(s[left]!=s[right]):
                return False
            left+=1
            right-=1
        return True
