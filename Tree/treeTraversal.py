class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A function to do inorder tree traversal
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val),
        printInorder(root.right)


# A function to do postorder tree traversal
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val),


# A function to do postorder tree traversal
def printPreorder(root):
    if root:
        print(root.val),
        printPreorder(root.left)
        printPreorder(root.right)


def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        # Use the larger one
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


def printLevelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        printGivenLevel(root, i)
        #Add this for level order traversal
        print("")


# Print nodes at a given level
def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.val,end=',')
    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)


# Given a binary tree, print its nodes in reverse level order
def reverseLevelOrder(root):
    q = []
    s = []
    q.append(root)

    while len(q) > 0:
        element = q.pop()
        s.append(element)

        if element.right is not None:
            q.append(element.right)

        if element.left is not None:
            q.append(element.left)

    while len(s) > 0:
        element = s.pop()
        print(element.val)


def printLeftTree(root):
    if root is not None:
        if root.left is not None:
            print(root.val)
            printLeftTree(root.left)
        elif root.right is not None:
            print(root.val)
            printLeftTree(root.right)

def printRightTree(root):
    if root is not None:
        if root.right is not None:
            printRightTree(root.right)
            print(root.val)
        elif root.left is not None:
            printRightTree(root.left)
            print(root.val)

def printLeaves(root):
    if root is not None:
        printLeaves(root.left)
        if root.left is None and root.right is None:
            print(root.val)
        printLeaves(root.right)

def printBoundary(root):
    if root is not None:
        print(root.val)

        printLeftTree(root.left)
        printLeaves(root.left)
        printLeaves(root.right)
        printRightTree(root.right)


if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    # root.left.left.left = Node(6)
    # root.left.left.left.left = Node(7)
    print("Preorder traversal of binary tree is")
    printPreorder(root)

    print("Inorder traversal of binary tree is")
    printInorder(root)

    print("Postorder traversal of binary tree is")
    printPostorder(root)

    h = height(root)
    print(f"Height is: {h}")

    print("Level order traversal of binary tree is -")
    printLevelOrder(root)

    print("Reverse Level order traversal of binary tree is -")
    reverseLevelOrder(root)

    root1 = Node(20)
    root1.left = Node(8)
    root1.left.left = Node(4)
    root1.left.right = Node(12)
    root1.left.right.left = Node(10)
    root1.left.right.right = Node(14)
    root1.right = Node(22)
    root1.right.right = Node(25)
    print("Boundary traversal is: ")
    printBoundary(root1)