#25题
#逆转链表每k个元素逆转一次
#参照第二道逆转题，先算出一个多少个节点
#如果剩余节点大于k，进入逆转循环，循环k次
#逆转一个片段后，把p0哨兵节点更新到逆转后的tail，也就是p0.next


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseK(self, head, k):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        dummy = ListNode(next=head)
        p0 = dummy
        pre = None
        cur = p0.next
        while n >= k:
            n -= k
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

            nxt = p0.next
            p0.next.next = cur
            p0.next = pre
            p0 = nxt

        return dummy.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    head2 = ListNode(5)
    print(Solution().reverseK(head2, 2))
