class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        
        diff=[]
        n=len(gas)
        total=0
        idx=0

        for i in range(n):
            diff.append(gas[i]-cost[i])
        
        for i in range(n):
            total+=diff[i]
            if total<0:
                total=0
                idx=i+1
        
        return idx
