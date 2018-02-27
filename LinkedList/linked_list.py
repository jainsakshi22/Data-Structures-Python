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
    def reverse_link_list(self, list):
        prev = None
        current = list.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        list.head = prev


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


    def compare_list(self, list1, list2):
        while list1 and list2:
            if list1.data == list2.data:
                list1 = list1.next
                list2 = list2.next
            else:
                return False

        if list1 is None and list2 is None:
            return True
        return False


    # Check if linked list is palindrome
    # 1) Get the middle of the linked list.
    # 2) Reverse the second half of the linked list.
    # 3) Check if the first half and second half are identical.
    # 4) Construct the original linked list by reversing the second half again and attaching it back to the first half
    def is_palindrome(self, head):
        slow_ptr = head
        fast_ptr = head
        prev_of_slow_ptr = head
        mid_node = None

        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            prev_of_slow_ptr = slow_ptr
            slow_ptr = slow_ptr.next

        # fast_ptr would become NULL when there are even elements in the list and not NULL for odd elements.
        # We need to skip the middle node for odd case and store it somewhere so that we can restore the original list
        if fast_ptr is not None:
            mid_node = slow_ptr
            slow_ptr = slow_ptr.next

        second_half = slow_ptr
        second_half.head = slow_ptr
        prev_of_slow_ptr.next = None

        # reverse second half
        self.reverse_link_list(second_half)

        isPalindrom = self.compare_list(head, second_half.head)

        # again reverse list
        self.reverse_link_list(second_half)
        if mid_node is not None:
            prev_of_slow_ptr.next = mid_node
            mid_node.next = second_half
        else:
            prev_of_slow_ptr.next = second_half

        return isPalindrom


    # Print reverse of a Linked List without actually reversing
    def print_reverse_list(self, current):
        current = current

        if current is None:
            return

        self.print_reverse_list(current.next)
        print(current.data)


    # Remove duplicates from a sorted linked list
    def remove_duplicate_sorted_list(self):
        current = self.head

        while current.next is not None:
            if current.data == current.next.data:
                next_next = current.next.next;
                current.next = None;
                current.next = next_next;
            else:
                current = current.next;


    # Remove duplicates from an unsorted linked list
    def remove_duplicate_unsorted_list(self):
        current = self.head
        s = set()
        prev = None

        while current is not None:
            if current.data in s:
                next = current.next
                prev.next = next
                current = None
                current = next
            else:
                s.add(current.data)
                prev = current
                current = current.next

    # Pairwise swap elements of a given linked list
    def pairwise_swap_elements_linklist(self):
        current = self.head
        while current is not None and current.next is not None:
            temp = current.data
            current.data = current.next.data
            current.next.data = temp
           # current.data, current.next.data = current.next.data, current.data
            current = current.next.next



if __name__=='__main__':

    llist = LinkedList()
    llist.insert_end(6)
    llist.insert_at_beginning(7)
    llist.insert_at_beginning(1)
    llist.insert_end(9)
    llist.insert_end(4)
    llist.insert_after(llist.head.next,8)

    print("Created linked list no 1 is: ")
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

    print("Reverse Linked list no 1")
    llist.reverse_link_list(llist)
    llist.print_linkedList()

    # llist.delete_linkedList()

    llist1 = LinkedList()
    llist1.insert_at_beginning(20)
    llist1.insert_at_beginning(15)
    llist1.insert_at_beginning(5)
    llist1.insert_at_beginning(2)

    # Create a loop for testing
    # Uncomment it to test loop
    # llist1.head.next.next.next.next = llist1.head.next;

    print("New looped linked list 2:")
    llist1.print_linkedList()

    if (llist1.detectLoop()):
        print("Loop found")
    else:
        print("No Loop ")

    llist2 = LinkedList()
    llist2.insert_at_beginning(22)
    llist2.insert_at_beginning(5)
    llist2.insert_at_beginning(3)
    llist2.insert_at_beginning(1)

    print("New linked list no 3:")
    llist2.print_linkedList()

    print("Merge linked list: 2 & 3 ")
    merged_list = LinkedList.merge_sorted_link_list(llist1, llist2)
    merged_list.print_linkedList()

    palindromeList = LinkedList()
    palindromeList.insert_at_beginning('a')
    palindromeList.insert_at_beginning('b')
    palindromeList.insert_at_beginning('d')
    palindromeList.insert_at_beginning('c')
    palindromeList.insert_at_beginning('d')
    palindromeList.insert_at_beginning('b')
    palindromeList.insert_at_beginning('a')

    print("palindrome list no 4 is: ")
    palindromeList.print_linkedList()
    if palindromeList.is_palindrome(palindromeList.head):
        print("List is palindrome")
    else:
        print("List is not palindrome")

    print("Print Reverse of reverse linked list 2")
    llist1.print_reverse_list(llist1.head)

    duplicateList = LinkedList()
    duplicateList.insert_at_beginning(11)
    duplicateList.insert_at_beginning(11)
    duplicateList.insert_at_beginning(11)
    duplicateList.insert_at_beginning(22)
    duplicateList.insert_at_beginning(43)
    duplicateList.insert_at_beginning(43)
    duplicateList.insert_at_beginning(54)

    print("Print duplicate item sorted list")
    duplicateList.print_linkedList()

    print("Delete duplicate item from duplicate list")
    duplicateList.remove_duplicate_sorted_list()
    duplicateList.print_linkedList()

    print("Make sorted duplicate list unsorted")
    duplicateList.insert_at_beginning(43)
    duplicateList.insert_at_beginning(11)
    duplicateList.print_linkedList()

    print("Delete duplicate elements from unsorted list")
    duplicateList.remove_duplicate_unsorted_list()
    print("List after removing duplicate items")
    duplicateList.print_linkedList()

    print("Pairwise Swap elemements")
    duplicateList.pairwise_swap_elements_linklist()
    duplicateList.print_linkedList()

