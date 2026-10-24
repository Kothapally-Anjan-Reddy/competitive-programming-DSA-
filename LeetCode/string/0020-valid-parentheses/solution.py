class Solution:

    def push(self,x):
        self.stack.append(x)

    def pop(self):
        if len(self.stack) ==0: return
        self.stack.pop()

    def peek(self):
        if len(self.stack) ==0: return
        return self.stack[-1]

    def isValid(self, s: str) -> bool:
        self.stack=[]
        dicti={'(':')','{':'}','[':']'}

        if len(s) % 2!=0: return False
        elif s[0] not in dicti.keys(): return False

        for i,ch in enumerate(s):
            if ch in dicti.keys():
                self.push(ch)
                
            elif dicti.get(self.peek())==ch:
                self.pop()

            else:
                return False

        
        return len(self.stack)==0
