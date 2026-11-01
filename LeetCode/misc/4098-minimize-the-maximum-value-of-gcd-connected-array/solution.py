class Solution:
    def minimumMaxValue(self, n: int, index: int, value: int) -> int:
        if value==1 or n==1:
            return -1
        
        divisor = value
        for d in range(2, int(value**0.5) + 1):
            if value % d == 0:
                divisor = d
                break

        right_steps=n-index-1
        left_steps=index
        if right_steps==0:
            end=value
        else:
            end=value+divisor+(2*(right_steps-1))
            
        if left_steps==0:
            start=value
        else:
            start=value-divisor-(2*(left_steps-1))


        return end if start>0 else -1
