class Solution:
    def assignUmbrella(self, rain: list[int]) -> list[str]:
        count=0
        answer=[]
        for i in range(len(rain)):
            if rain[i]==0:
                answer.append("None")
            elif i+1<len(rain) and rain[i]==1 and rain[i+1]==1 and count<=0:
                count+=1
                answer.append("Alice")
            else:
                answer.append("Bob")
                count-=1
        
        return answer
