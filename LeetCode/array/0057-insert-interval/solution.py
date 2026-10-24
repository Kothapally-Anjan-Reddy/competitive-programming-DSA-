class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # res=[]
        # for i in range(len(intervals)):
        #     if newInterval[1] < intervals[i][0]:
        #         res.append(newInterval)
        #         return res+intervals[i:]
        #     elif newInterval[0] > intervals[i][1]:
        #         res.append(intervals[i])
        #     else:
        #         newInterval=[
        #             min(intervals[i][0],newInterval[0]),
        #             max(intervals[i][1],newInterval[1])
        #         ]
        
        # res.append(newInterval)
        # return res


        res=[]
        new_start,new_end=newInterval
        for i,(start,end) in enumerate(intervals):
            if new_end < start:
                res.append([new_start,new_end])
                return res+intervals[i:]
            elif new_start > end:
                res.append(intervals[i])
            else:
                new_start=min(start,new_start)
                new_end=max(end,new_end)
        
        res.append([new_start,new_end])

        return res
