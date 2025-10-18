#1721 链表交换元素 不太好写需要注意dummy套两层，

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 拿到第k个位置前一个位置的node

        fast = ListNode(20, head)
        dummy = ListNode(60, fast)##################关键
        for _ in range(k - 1):
            fast = fast.next
        front_knode_prev = fast
        fast = fast.next
        slow = dummy.next #####################关键
        # slow和fast一起直到fast到结尾
        while fast.next:
            fast = fast.next
            slow = slow.next
        back_knode_prev = slow

        front_prev = front_knode_prev
        front = front_prev.next
        front_next = front.next

        back_prev = back_knode_prev
        back = back_prev.next
        back_next = back.next
        #print(f"dummy = {dummy.val}front = {front.val} back = {back.val} front_prev={front_prev.val}, back_prev = {back_prev.val}")
        # 如果相邻特殊处理：
        if front.next == back:
            front_prev.next = back
            back.next = front
            front.next = back_next
            return dummy.next.next
        if back.next == front:
            back_prev.next = front
            front.next = back
            back.next = front_next
            return dummy.next.next

        front_prev.next = back
        back.next = front_next

        back_prev.next = front
        front.next = back_next

        return dummy.next.next
