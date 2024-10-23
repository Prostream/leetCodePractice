# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        pointer1 = ListNode(0)
        pointer2 = ListNode(0)
        pointer1.next = list1
        pointer2.next = list2

        dummy = ListNode()
        ans_with_head = dummy
        while pointer1.next is not None and pointer2.next is not None:
            if pointer1.next.val <= pointer2.next.val:
                ans_with_head.next = pointer1.next
                pointer1.next = pointer1.next.next
            elif pointer2.next.val < pointer1.next.val:
                ans_with_head.next = pointer2.next
                pointer2.next = pointer2.next.next
            ans_with_head = ans_with_head.next

        if pointer1.next is None:#
            ans_with_head.next = pointer2.next
        else:
            ans_with_head.next = pointer1.next

        return dummy


