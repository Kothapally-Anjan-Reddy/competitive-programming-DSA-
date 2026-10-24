class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        window={}
        frequency={}
        for i in s1:
            frequency[i]=frequency.get(i,0)+1

        l=0
        r=0
        for r in range(len(s2)):
            window[s2[r]]=window.get(s2[r],0)+1     #If there is for loop then we frst add the element in the dictionary before using any condition to increment.
            if (r-l+1)>len(s1):
                window[s2[l]]=window.get(s2[l])-1
                if window[s2[l]]==0:
                    del window[s2[l]]
                l+=1
            if window==frequency:
                return True
        return False
