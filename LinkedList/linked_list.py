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

        # If deleted node is head
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
    # Take 2 pointers
    def find_middle_linkList(self):
        slow_ptr = self.head
        fast_ptr = self.head

        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        return slow_ptr.data


    # Take 2 pointers. Take reference point to n, then iterate main and reference ptr till reference ptr reaches end.
    # Main ptr will return the nth node from end.
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


    # Main point here is not to access next of the current pointer if current pointer is deleted
    def delete_linkedList(self):
        temp = self.head
        while temp:
            next = temp.next
            temp = None
            temp = next


    # Function to reverse the linked list. Din't get the concept
    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


    # Check whether there is loop in linked list
    def detect_loop(self):
        s = set()
        temp = self.head
        while temp:
            if temp in s:
                return True
            s.add(temp)
            temp = temp.next
        return False

    # Move one pointer by one and other pointer by two.  If these pointers meet at some node then there is a loop.
    # If pointers do not meet then linked list doesn’t have loop
    def detectLoop(self):
        slow_p = self.head
        fast_p = self.head
        while (slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return True
        return False


    # Merge two sorted link list
    @staticmethod
    def merge_sorted_link_list(list1, list2):
        temp1 = list1.head
        temp2 = list2.head
        new_list = LinkedList()

        while temp1 is not None or temp2 is not None:
            if temp1 is None and temp2 is not None:
                while temp2:
                    new_list.insert_end(temp2.data)
                    temp2 = temp2.next
            elif temp2 is None and temp1 is not None:
                while temp1:
                    new_list.insert_end(temp1.data)
                    temp1 = temp1.next
            else:
                if temp1.data > temp2.data:
                    new_list.insert_end(temp2.data)
                    temp2 = temp2.next
                elif temp1.data < temp2.data:
                    new_list.insert_end(temp1.data)
                    temp1 = temp1.next
                else:
                    new_list.insert_end(temp2.data)
                    new_list.insert_end(temp1.data)
                    temp2 = temp2.next
                    temp1 = temp1.next

        return new_list


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

    print("Reverse Linked list")
    llist.reverse()
    llist.print_linkedList()

    # llist.delete_linkedList()

    llist1 = LinkedList()
    llist1.insert_at_beginning(20)
    llist1.insert_at_beginning(15)
    llist1.insert_at_beginning(5)
    llist1.insert_at_beginning(2)

    print("New looped linked list:")
    llist1.print_linkedList()

    llist2 = LinkedList()
    llist2.insert_at_beginning(22)
    llist2.insert_at_beginning(5)
    llist2.insert_at_beginning(3)
    llist2.insert_at_beginning(1)

    print("New looped linked list:")
    llist2.print_linkedList()

    # Create a loop for testing
    # Uncomment it to test loop
    # llist1.head.next.next.next.next = llist1.head.next;

    if (llist1.detectLoop()):
        print("Loop found")
    else:
        print("No Loop ")

    print("Merge two linked list: ")
    merged_list = LinkedList.merge_sorted_link_list(llist1, llist2)
    merged_list.print_linkedList()
    