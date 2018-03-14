from stack import Stack

class StandardProblem(Stack):

    def isMatchingPair(self, op):
        a = self.pop()
        if a == '(' and op == ')':
            return True
        elif a == '{' and op == '}':
            return True
        elif a == '[' and op == ']':
            return True
        return False

    def areParenthesisBalanced(self, exp):
        for i in exp:
            if i == '(' or i == '{' or i == '[':
                self.push(i)
            elif i == ')' or i == '}' or i == ']':
                if self.isEmpty():
                    print("Not Balanced")
                    return False
                elif not self.isMatchingPair(i):
                    print("Not Balanced")
                    return False

        if self.isEmpty():
            print("Balanced")
            return True
        print("Not Balanced")
        return False

    # The Next greater Element for an element x is the first greater element on the right side of x in array.
    # Elements for which no greater element exist, consider next greater element as -1
    def nextGreaterElement(self, arr):
        element = 0
        next = 0

        # push the first element to stack
        self.push(arr[0])

        # iterate for rest of the elements
        for i in range(1, len(arr), 1):
            next = arr[i]

            if not self.isEmpty():

                # if stack is not empty, then pop an element from stack
                element = self.pop()

                '''If the popped element is smaller than next, then
                    a) print the pair
                    b) keep popping while elements are smaller and
                       stack is not empty '''
                while element < next:
                    print(str(element) + " -- " + str(next))
                    if self.isEmpty():
                        break
                    element = self.pop()

                '''If element is greater than next, then push
                   the element back '''
                if element > next:
                    self.push(element)

            '''push next to stack so that we can find
               next greater for it '''
            self.push(next)

        '''After iterating over the loop, the remaining
           elements in stack do not have the next greater
           element, so print -1 for them '''

        while self.isEmpty() == False:
            element = self.pop()
            next = -1
            print(str(element) + " -- " + str(next))


    #Check concept. Currently copied paste for debugging
    def towerOfHanoi(self, n, from_rod, to_rod, aux_rod):
        if n == 1:
            print("Move disk 1 from rod", from_rod, "to rod", to_rod)
            return
        self.towerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
        print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
        self.towerOfHanoi(n - 1, aux_rod, to_rod, from_rod)

    # Check concept. Currently copied paste for debugging
    # First pops all stack items and stores the popped item in function call stack using recursion.
    # And when stack becomes empty, pushes new item and all items stored in call stack
    def insertAtBottom(self, item):
        if self.isEmpty():
            self.push(item)
        else:
            temp = self.pop()
            self.insertAtBottom(item)
            self.push(temp)

    # Check concept. Currently copied paste for debugging
    # Below is the function that reverses the given stack using insertAtBottom()
    def reverse(self):
        if not self.isEmpty():
            temp = self.pop()
            self.reverse()
            self.insertAtBottom(temp)


    def sortedInsert(self, item):
        if self.isEmpty() or item < self.peek():
            self.push(item)
        else:
            temp = self.pop()
            self.sortedInsert(item)
            self.push(temp)

    def sortStack(self):
        if not self.isEmpty():
            temp = self.pop()
            self.sortStack()
            self.sortedInsert(temp)


class Celebrity(Stack):
    def __init__(self):
        super().__init__()
        self.matrix = [[0, 0, 1, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 0],
                       [0, 0, 1, 0]]

    def knowsPerson(self, a, b):
        return True if self.matrix[a][b] == 1 else False

    def findCelebrity(self, n):
        for i in range(n):
            self.push(i)

        while self.root.next is not None:
            a = self.pop()
            b = self.pop()

            if self.knowsPerson(a, b):
                self.push(b)
            else:
                self.push(a)

        c = self.pop()

        # Check whether c is celebrity or not
        for i in range(n):
            if i != c:
                ''' If c knows any person or
                any person doesn't know c, then c is not celebrity'''
                if self.knowsPerson(c, i) or not self.knowsPerson(i, c):
                    print("Celebrity not found")
                    return -1
        print("Celebrity found")
        return c



if __name__=='__main__':
    exp = ['{','(',')','}','[',']']
    paranObj = StandardProblem()
    paranObj.areParenthesisBalanced(exp)


    arr = [11, 13, 21, 3]
    paranObj.nextGreaterElement(arr)


    celebrity = Celebrity()
    print(celebrity.findCelebrity(4))


    obj = StandardProblem()
    n = 4
    obj.towerOfHanoi(n, 'A', 'C', 'B')


    stackObj = StandardProblem()
    stackObj.push(str(4))
    stackObj.push(str(3))
    stackObj.push(str(2))
    stackObj.push(str(1))
    print("Original Stack ")
    stackObj.print_stack()

    stackObj.reverse()
    print("Reversed Stack ")
    stackObj.print_stack()


    sortObj = StandardProblem()
    sortObj.push(30)
    sortObj.push(-5)
    sortObj.push(14)
    sortObj.push(18)
    sortObj.push(14)
    sortObj.push(-3)
    print("Original Stack ")
    sortObj.print_stack()

    sortObj.sortStack()

    print("Sorted Stack ")
    sortObj.print_stack()
