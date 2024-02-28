from collections import deque

class MyStack:

    def __init__(self):
        self.lst=deque()

    def push(self, x: int) -> None:
        self.lst.append(x)

    def pop(self) -> int:
        for i in range(len(self.lst)-1):
            self.lst.append(self.lst.popleft())
        return self.lst.popleft()

    def top(self) -> int:
        return self.lst[-1]

    def empty(self) -> bool:
        return len(self.lst)==0
    

#Your MyStack object will be instantiated and called as such:
#obj = MyStack()
#obj.push(x)
#param_2 = obj.pop()
#param_3 = obj.top()
#param_4 = obj.empty()