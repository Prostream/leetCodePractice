# 61题，旋转链表
# 把链表变成一个环，然后断掉需要断的那一个位置
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        cur = head
        n = 1
        while cur.next:
            n += 1
            cur = cur.next

        cur.next = head

        #建好环，准备好新的头节点，并且断掉第n-k%n个节点的next

        cur = head
        for _ in range(n-k%n - 1):
            cur = cur.next
        head = cur.next
        cur.next = None

        return head



