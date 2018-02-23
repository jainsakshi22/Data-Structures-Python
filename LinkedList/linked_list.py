class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Inserts a new node after the given previous_node
    def insert_after(self, previous_node, new_data):

        if previous_node is None:
            print("The previous node is not in linked list")
            return

        new_node = Node(new_data)
        new_node.next = previous_node.next
        previous_node.next = new_node


    # Insert a new node at the end
    def insert_end(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while (last_node.next):
            last_node = last_node.next

        last_node.next = new_node


    # Print linked list
    def print_linkedList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

if __name__=='__main__':

    llist = LinkedList()
    llist.insert_end(6)
    llist.insert_at_beginning(7)
    llist.insert_at_beginning(1)
    llist.insert_end(4)
    llist.insert_after(llist.head.next,8)

    print("Created linked list is: ")
    llist.print_linkedList()