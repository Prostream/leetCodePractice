# 141
# 探测链表有没有环，快慢指针法呗，
# 一个一次走一步，一个一次走两步，
# （在快指针到尾巴前截至）
# 如果相遇就有环
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

