class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        res=""
        if sum>9*num:
            return res

        count,rem=sum//9, sum%9

        while len(res)<num:
            if count>0:
                res+='9'
                count-=1
            elif rem>0:
                res+=str(rem)
                rem=0
            else:
                res+='0'

        return res
