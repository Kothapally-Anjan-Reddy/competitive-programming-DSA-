class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        odd,even=0,0  #odd is no.of subarrays ending at current index with odd sum
        ans=0
        MOD=((10**9)+7)
        for num in arr:
            if num%2!=0:
                even,odd=odd,even+1
            else:
                even,odd=even+1,odd
            ans=(ans+odd)%MOD
        return ans
