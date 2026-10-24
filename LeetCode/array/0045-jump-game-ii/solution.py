from collections import deque
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
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
                return level
            for i in range(x+1,min(len(nums)-1,farthest)+1):
                q.append(i)

        return level
