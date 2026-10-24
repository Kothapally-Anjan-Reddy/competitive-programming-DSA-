class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def dict_max():
            # return max(frequency,key=frequency.get)     #For getting the key even thorugh the max is found between values
            return max(frequency.values())

        if len(s)<2:
            return len(s)
        l=0
        r=0
        frequency={}
        max_count=float('-inf')
        while r<len(s):
            frequency[s[r]]=frequency.get(s[r],0)+1
            if (r-l+1-dict_max())>k:
                frequency[s[l]]=frequency.get(s[l])-1
                l+=1
            max_count=max(max_count,r-l+1)
            r+=1        # Here the r must incremented after the max_count is calculated as it will use the value r if its changed first then it will go out of bounds at end and at each iteration 1 will be wrong

        return max_count
