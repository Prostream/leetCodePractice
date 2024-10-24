#24
#给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            node1 = prev.next
            node2 = prev.next.next

            prev.next = node2
            node1.next = node2.next
            node2.next = node1

            prev = node1

        return dummy.next
