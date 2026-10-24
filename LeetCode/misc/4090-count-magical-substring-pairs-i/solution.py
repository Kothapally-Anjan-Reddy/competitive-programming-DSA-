class Solution:
    def countMagicalPairs(self, s: str) -> int:
        res=0
        Str=s
        
        for j in range(len(s)-1):
            left_distinct=[]
            right_distinct=[]
            left_count=[0]*26
            right_count=[0]*26
            distinct=0
            for i in range(j,-1,-1):
                idx=ord(Str[i])-ord('a')
                if left_count[idx]==0:
                    distinct+=1
                left_count[idx]+=1
                left_distinct.append(distinct)

            distinct=0
            for k in range(j+1,len(s)):
                idx=ord(Str[k])-ord('a')
                if right_count[idx]==0:
                    distinct+=1
                right_count[idx]+=1
                right_distinct.append(distinct)

            freq=[0]*27
            for d in left_distinct:
                freq[d]+=1
            for d in right_distinct:
                res+=freq[d]
        return res


# Variable	Purpose
# j	The position where the first substring ends
# i	Moves backward to create all left substrings
# k	Moves forward to create all right substrings
# left_count	Tracks character frequencies in the current left substring
# right_count	Tracks character frequencies in the current right substring
# left_distinct	Stores the distinct-character count for each left substring
# right_distinct	Stores the distinct-character count for each right substring
# freq	Counts how often each distinct-character count appears on the left
# res	Total number of magical pairs
