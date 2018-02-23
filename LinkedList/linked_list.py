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


    # This function counts number of nodes in Linked List
    def length_linked_list(self):
        temp = self.head
        length = 0
        while temp is not None:
            length += 1
            temp = temp.next
        return length


    # Search a key in linked list
    def search_an_element(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False


    # Swap nodes in a linked list without swapping data
    # Important case when we have to swap adjacent elements
    def swap_nodes(self, key1, key2):
        temp1 = self.head
        temp2 = self.head
        prev1 = None
        prev2 = None
        while temp1:
            if temp1.data == key1:
                break
            prev1 = temp1
            temp1 = temp1.next

        while temp2:
            if temp2.data == key2:
                break
            prev2 = temp2
            temp2 = temp2.next

        if temp1 is None or temp2 is None:
            return

        if prev1:
            prev1.next = temp2
        else:
            self.head = temp2

        if prev2:
            prev2.next = temp1
        else:
            self.head = temp1

        temp = temp1.next
        temp1.next = temp2.next
        temp2.next = temp

    # Find the middle of a given linked list
    def find_middle_linkList(self):
        slow_ptr = self.head
        fast_ptr = self.head

        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        return slow_ptr.data


    def print_nth_element_from_last(self, n):
        main_ptr = self.head
        ref_ptr = self.head

        if self.head:
            for i in range(n):
                if ref_ptr is None:
                    print("index out of scope")
                    return
                ref_ptr = ref_ptr.next

        while ref_ptr:
            ref_ptr = ref_ptr.next
            main_ptr = main_ptr.next

        return main_ptr.data


if __name__=='__main__':

    llist = LinkedList()
    llist.insert_end(6)
    llist.insert_at_beginning(7)
    llist.insert_at_beginning(1)
    llist.insert_end(9)
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

    print("Length of linked list is: ", llist.length_linked_list())

    print("Search element 8 in linked list: ", llist.search_an_element(8))

    print("Swap elements 8 & 6")
    llist.swap_nodes(8, 6)
    print("Linked list after swap: ")
    llist.print_linkedList()

    print("Find middle of linked list", llist.find_middle_linkList())

    print("Print 3rd element from last", llist.print_nth_element_from_last(3))