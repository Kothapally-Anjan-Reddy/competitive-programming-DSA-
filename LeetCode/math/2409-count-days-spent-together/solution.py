class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        no_of_days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        dates=[]
        for event in [arriveAlice,leaveAlice,arriveBob,leaveBob]:
            start_month=int(event[:2])
            start_day=-1
            for i in range(start_month-1):
                start_day+=no_of_days[i]
            start_day+=int(event[3:5])
            dates.append(start_day)
        
        if dates[1]<dates[2] or dates[3]<dates[0]:
            return 0
        else:
            return min(dates[1],dates[3])-max(dates[0],dates[2])+1
