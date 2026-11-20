class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            new_str=""
            total=0
            for i in range(len(s)):
                if i%k==0:
                    new_str+=str(total)
                    total=int(s[i])
                else:
                    total+=int(s[i])
            new_str+=str(total)
            s=new_str[1:]
        
        return s
