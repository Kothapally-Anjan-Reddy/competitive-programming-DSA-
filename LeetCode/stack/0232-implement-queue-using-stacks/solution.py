class MyQueue:

    def __init__(self):
        self.q1=[]
        self.q2=[]

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        if self.empty(): return
        while len(self.q1)!=0:
            self.q2.append(self.q1.pop())
        result=self.q2.pop()
        while len(self.q2)!=0:
            self.q1.append(self.q2.pop())
        return result

    def peek(self) -> int:
        if self.empty(): return
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
