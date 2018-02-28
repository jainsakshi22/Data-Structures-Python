from stack import Stack

class Queue:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enQueue(self, data):
        self.stack1.push(data)
        print(f"{data} pushed to queue")

    def deQueue(self):
        if self.stack1.isEmpty() and self.stack2.isEmpty():
            print("Queue is empty")
            return

        if self.stack2.isEmpty():
            while not self.stack1.isEmpty():
                x = self.stack1.pop()
                self.stack2.push(x)
        x = self.stack2.pop()
        return x

if __name__=='__main__':
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)

    print(f"Poppped element is: {q.deQueue()}")
    print(f"Poppped element is: {q.deQueue()}")

