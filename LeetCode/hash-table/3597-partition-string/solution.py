class Solution:
    def partitionString(self, s: str) -> List[str]:
        unique=set()
        res=[]
        string=""

        for i in s:
            string+=i
            if string not in unique:
                unique.add(string)
                res.append(string)
                string=""
        
        return res
