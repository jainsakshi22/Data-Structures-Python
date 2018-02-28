class StackNode:

    # Constructor to initialize a node
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    # Constructor to initialize the root of linked list
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return True if self.root is None else False

    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.root
        self.root = newNode

    def pop(self):
        if (self.isEmpty()):
            return float("-inf")
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        temp = None
        return popped

    def peek(self):
        if self.isEmpty():
            return float("-inf")
        return self.root.data

    def print_stack(self):
        current = self.root
        while current:
            print(current.data)
            current = current.next

if __name__=='__main__':
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    stack.print_stack()
    print("popped from stack", (stack.pop()))
    print("Top element is", (stack.peek()))
    stack.print_stack()