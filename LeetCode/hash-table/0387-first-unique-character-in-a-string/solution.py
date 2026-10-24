class Solution:
    def firstUniqChar(self, s: str) -> int:
        characters={}
        required=0
        for index,i in enumerate(s):
            if(i in characters):
                characters[i]=characters.get(i) + 1
            else:
                characters.update({i:1})
        for key,value in characters.items():
            if(value==1):
                required=key
                break
        for i,char in enumerate(s):
            if(char==required): return i
        return -1
