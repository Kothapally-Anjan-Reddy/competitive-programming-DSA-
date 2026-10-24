class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        if len(t)==1:
            return [0]
        output=[0]*len(t)
        stack=[]
        for ind,i in enumerate(t):
            while stack and i>stack[-1][1]:               
                stackin,stackt=stack.pop()
                output[stackin]=ind-stackin
            stack.append([ind,i])
        
        return output
