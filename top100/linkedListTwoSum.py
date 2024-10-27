# 2
from multiprocessing import dummy


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummpy = ListNode(0)
        current = dummpy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total_val = val1 + val2 + carry
            carry = total_val // 10
            new_val = total_val % 10

            current.next = ListNode(new_val)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummpy.next

if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l2 = ListNode(4)
    l2.next = ListNode(5)
    l2.next.next = ListNode(6)
    print(Solution().addTwoNumbers(l1, l2).val)