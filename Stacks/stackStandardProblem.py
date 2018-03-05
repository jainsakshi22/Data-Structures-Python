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



if __name__=='__main__':
    exp = ['{','(',')','}','[',']']
    paranObj = StandardProblem()
    paranObj.areParenthesisBalanced(exp)

    arr = [11, 13, 21, 3]
    paranObj.nextGreaterElement(arr)
