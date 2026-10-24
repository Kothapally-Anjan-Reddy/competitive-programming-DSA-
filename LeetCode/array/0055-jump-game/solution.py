
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # goal=len(nums)-1

        # for i in range(len(nums)-1,-1,-1):
        #     if  i+nums[i]>=goal:
        #         goal=i
        
        # return goal==0

        if len(nums)==1:
            return True
        q=deque()
        q.append(0)
        level=0

        while q:
            farthest=0
            n=q[0]
            for i in range(len(q)):
                x=q.popleft()
                dist=x+nums[x]
                if dist>farthest:
                    n=x
                farthest=max(dist,farthest)
            level+=1
            if farthest>=len(nums)-1:
                return True
            for i in range(x+1,min(len(nums)-1,farthest)+1):
                q.append(i)

        return False
