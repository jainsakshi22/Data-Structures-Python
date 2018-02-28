from stack import Stack

class SpecialStack(Stack):
    def __init__(self):
        self.stack = Stack()
        self.minStack = Stack()

    def push(self, data):
        if self.stack.isEmpty():
            self.minStack.push(data)
            self.stack.push(data)
        else:
            x = self.stack.peek()
            if x > data:
                self.minStack.push(data)
            else:
                self.minStack.push(x)
            self.stack.push(data)

    def getMin(self):
        x = self.minStack.pop()
        self.stack.pop()
        return x


if __name__=='__main__':
    s = SpecialStack()
    s.push(10)
    s.push(20)
    s.push(30)
    print(f"Min element is: {s.getMin()}")
    s.push(5);
    print(f"Min element is: {s.getMin()}")

