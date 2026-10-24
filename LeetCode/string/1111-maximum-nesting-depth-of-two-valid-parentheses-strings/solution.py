class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        depthA=0
        depthB=0
        res=[]
        openingA,openingB=0,0

        for i,n in enumerate(seq):
            if n=='(':
                if depthA<=depthB:
                    res.append(0)
                    openingA+=1
                    depthA+=1
                else:
                    res.append(1)
                    openingB+=1
                    depthB+=1
            else:
                if openingA>=openingB:
                    res.append(0)
                    openingA-=1
                    depthA-=1
                else:
                    res.append(1)
                    openingB-=1
                    depthB-=1
        
        return res
