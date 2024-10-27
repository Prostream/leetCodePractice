#138 133题克隆图类似
# 要求我们复制一个带有随机指针的链表。
# 用hash表复制linklist1的所有节点
# 遍历第二次，简历拷贝linkedlist的指针关系
from twoPointer.linked_list import LinkedList


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random



class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        dummpy = Node(0)
        copy_linked_pointer = dummpy
        node_table = {}

        original_pointer = head
        while original_pointer:
            copy_linked_pointer.val = original_pointer.val

            node_table[original_pointer] = copy_linked_pointer
            original_pointer = original_pointer.next

            copy_linked_pointer_next = Node(original_pointer.val)
            copy_linked_pointer.next = copy_linked_pointer_next
            copy_linked_pointer = copy_linked_pointer.next

        original_pointer = head
        #第二次遍历
        while original_pointer:
            if original_pointer.random in node_table:
                copy_random = node_table[original_pointer.random]
                coyp_current = node_table[original_pointer]
                coyp_current.random = copy_random
            elif not original_pointer.random:
                coyp_current = node_table[original_pointer]
                coyp_current.random = None
            original_pointer = original_pointer.next

        return dummpy






