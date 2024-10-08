#2 两个链表数相加
# Definition for singly-linked list.
# 应该是采用双指针法处理
#
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()  # 创建一个虚拟头节点
        current = dummy  # 用于追踪结果链表的当前节点
        carry = 0  # 初始化进位为 0

        while l1 or l2 or carry:
            # 如果 l1 或 l2 为空，直接取 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # 计算当前位的总和及进位
            total = val1 + val2 + carry
            carry = total // 10  # 进位
            new_val = total % 10  # 当前位的结果

            # 把计算结果放到新的节点上
            current.next = ListNode(new_val)
            current = current.next

            # 移动 l1 和 l2 指针
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # 返回结果链表，跳过虚拟头节点
        return dummy.next

if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    print(Solution().addTwoNumbers(l1, l2))