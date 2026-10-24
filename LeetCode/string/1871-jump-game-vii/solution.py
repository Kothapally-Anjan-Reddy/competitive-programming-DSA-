class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1]=='1':
            return False

        farthest=0
        q=deque()
        q.append(0)

        while q:
            x=q.popleft()
            for j in range(max(farthest+1,x+minJump),min(len(s)-1,x+maxJump)+1):
                if s[j]=='0':    
                    if j==len(s)-1:
                        return True
                    q.append(j)

            farthest=x+maxJump
        return False
