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

    # Delete node with key passed as parameter
    def delete_node(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None



    # Python program to delete a node in a linked list at a given position
    def delete_node_at_position(self, position):

        temp = self.head

        if self.head == None:
            return

        if position == 0:
            self.head = temp.next
            temp = None
            return

        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return
        if temp.next is None:
            return

        node_to_delete = temp.next
        temp.next = None
        temp.next = node_to_delete.next


if __name__=='__main__':

    llist = LinkedList()
    llist.insert_end(6)
    llist.insert_at_beginning(7)
    llist.insert_at_beginning(1)
    llist.insert_end(4)
    llist.insert_after(llist.head.next,8)

    print("Created linked list is: ")
    llist.print_linkedList()

    print("Delete element: 7")
    llist.delete_node(7)

    print("linked list after deleting element is: ")
    llist.print_linkedList()

    print("Delete element at position 1")
    llist.delete_node_at_position(3)

    print("linked list after deleting element is: ")
    llist.print_linkedList()