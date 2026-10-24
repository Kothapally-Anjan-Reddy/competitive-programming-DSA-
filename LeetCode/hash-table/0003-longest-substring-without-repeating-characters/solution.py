class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=1
        hashe={}
        if(len(s)==1 or len(s)==0):
                return len(s)
        maxi=1
        sub=s[0]
        hashe.update({s[left]:1})

        while(right<len(s)):
            while(s[right] in hashe):
                del hashe[s[left]]
                left+=1
            sub+=s[right]
            hashe.update({s[right]:1})
            right+=1
            maxi=max(maxi,right-left)

        return maxi
