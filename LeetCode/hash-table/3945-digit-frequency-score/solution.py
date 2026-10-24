class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        frequency={}
        m=n
        while m!=0:
            i=m%10
            m=m//10
            frequency[i]=frequency.get(i,0)+1
        
        frequency=list(frequency.items())
        res=0
        for i in range(0,len(frequency)):
            res+=frequency[i][0]*frequency[i][1]

        return res
