class Solution:
    def reverse(self, x: int) -> int:
        neg=0
        if x<0:
            neg=1
        x=int(str(abs(x))[::-1])
       
        if x > math.pow(2,31)-1 or x< -(math.pow(2,31)):
            return 0
       
        return x if neg==0 else -x
