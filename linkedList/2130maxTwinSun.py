from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def pairSum(self, head: Optional[ListNode]) -> int:
    # 快慢指针找中点
    mid = None
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        mid = slow
        slow = slow.next
    mid.next = None
    # 到mid为止，需要逆转
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    new_head = prev

    # 两条链一起计算
    max_pair = 0
    while new_head:
        max_pair = max(max_pair, new_head.val + slow.val)
        new_head = new_head.next
        slow = slow.next

    return max_pair