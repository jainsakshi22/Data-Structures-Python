#from linked_list import *
from linked_list import LinkedList

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

    print("Pairwise Swap elemements by adding 5 in end")
    duplicateList.insert_end(5)
    duplicateList.pairwise_swap_elements_linklist()
    duplicateList.print_linkedList()

    print("Move last element to front")
    duplicateList.move_last_element_tofront()
    duplicateList.print_linkedList()

    # duplicateList.insert_end(6)
    # print("Print list after adding 6")
    # duplicateList.print_linkedList()
    print("Delete alternate elements")
    duplicateList.delete_alternate_nodes()
    duplicateList.print_linkedList()

    identicalList = LinkedList()
    identicalList.insert_at_beginning(54)
    identicalList.insert_at_beginning(11)
    identicalList.insert_at_beginning(5)
    print("Identical list to duplicate list is:")
    identicalList.print_linkedList()

    if duplicateList.areIdentical(identicalList):
        print("Lists are identical")
    else:
        print("Lists are not identical")
