# Create a data structure twoStacks that represents two stacks. Implementation of twoStacks should use only one array
class TwoStacks:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        self.top1 = -1
        self.top2 = size

    # push1(x) –> pushes x to first stack
    def push1(self, data):
        if self.top1 < self.top2 - 1:
            self.top1 = self.top1 + 1
            self.arr[self.top1] = data
        else:
            print("Stack overflow")
            exit(1)

    def push2(self, data):
        if self.top1 < self.top2 - 1:
            self.top2 = self.top2 - 1
            self.arr[self.top2] = data
        else:
            print("Stack overflow")
            exit(1)

    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 = self.top1 - 1
            return x
        else:
            print("Stack Underflow")
            exit(1)

    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 = self.top2 + 1
            return x
        else:
            print("Stack Underflow")
            exit(1)


if __name__=='__main__':
    ts = TwoStacks(5)
    ts.push1(5)
    ts.push2(10)
    ts.push2(15)
    ts.push1(11)
    ts.push2(7)

    print("Popped element from stack1 is " + str(ts.pop1()))
    ts.push2(40)
    print("Popped element from stack2 is " + str(ts.pop2()))