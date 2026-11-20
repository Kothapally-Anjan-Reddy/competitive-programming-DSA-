class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            new_str=""
            total=0
            for i in range(0,len(s),k):
                chunk=s[i:i+k]
                total=sum(int(digit) for digit in chunk)
                new_str+=str(total)
            s=new_str
        
        return s
