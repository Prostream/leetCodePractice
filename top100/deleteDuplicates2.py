# 82
# 删除链表中所有重复val的节点
# 遍历两次，第一次计数
# 第二次看这个节点是不是属于要删除的
from multiprocessing import dummy


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dict_val = {}
        cur = head
        while cur:
            if cur.val not in dict_val:
                dict_val[cur.val] = 1
            else:
                dict_val[cur.val] += 1
            cur = cur.next

        #第二次遍历
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head
        while cur:
            if dict_val[cur.val] >= 2:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next

        return dummy.next

