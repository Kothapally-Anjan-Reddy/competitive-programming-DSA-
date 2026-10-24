class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        intervals.sort()
        prev=intervals[0]

        for current in intervals[1:]:
            if prev[1]<current[0]:
                res.append(prev)
                prev=current
            else:
                prev=[min(current[0],prev[0]),max(current[1],prev[1])]
        
        res.append(prev)
        return res
