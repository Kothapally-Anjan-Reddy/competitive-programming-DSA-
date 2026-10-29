class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        specials=[]
        start=0
        total=0
        for i in range(len(s)):
            total+= (+1 if s[i]=='1' else -1)
            if total==0:
                inner=s[start+1:i]
                specials.append('1'+self.makeLargestSpecial(inner)+'0')
                start=i+1

        specials.sort(reverse=True)
        res=""
        for i in specials:
            res+=i
        
        return res
