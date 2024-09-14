from linked_list import LinkedList

def get_middle_node(head):
    #slow和fast两个pointer
    slow = head
    fast = head
    #遍历linkedList，直到fast.next is none or fast is none
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow