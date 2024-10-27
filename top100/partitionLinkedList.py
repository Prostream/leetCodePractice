#86
#链表二分，把小于k的节点放左边，大于等于k的节点放右边
# 俩个子链表，然后连起来
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from top100.MergeLink import ListNode


class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        dummy1 = ListNode(0)
        head1 = dummy1
        dummy2 = ListNode(0)
        head2 = dummy2
        cur = head
        while cur:
            if cur.val < x:
                head1.next = cur
                head1 = head1.next
            else:
                head2.next = cur
                head2 = head2.next
            cur = cur.next

        #断掉可能出现的环
        head2.next = None
        head1.next = dummy2.next
        return dummy1.next

