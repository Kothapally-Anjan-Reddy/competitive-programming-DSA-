class Solution:
    def longestPalindrome(self, s: str) -> str:
            longest,start,end=0,0,0

            def max_palin(l,r):
                nonlocal longest,start,end
                while l>=0 and r<len(s) and s[l]==s[r]:
                    if r-l+1>longest:
                        longest,start,end=r-l+1,l,r
                    l-=1
                    r+=1

            for i in range(len(s)):
                # For odd cases:
                max_palin(i,i)

                # For even cases:
                max_palin(i,i+1)
                
            return s[start:end+1]
