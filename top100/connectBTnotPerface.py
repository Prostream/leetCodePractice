from collections import deque
from unittest.mock import right


#11 不完美二叉树每层连起来
# 层序遍历 维护一下每一层的信息（可以考虑在队列里维护一层的开始和结束）
# 也可以考虑用父节点的next来找 用这个就不需要队列了
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None:
            return None
        cur_root = root
        while cur_root:
            dummpy_child = Node(0)
            tail = dummpy_child
            #把子节点连起来
            while cur_root:
                if cur_root.left:
                    tail.next = cur_root.left
                    tail = tail.next
                if cur_root.right:
                    tail.next = cur_root.right
                    tail = tail.next
                cur_root = cur_root.next
            cur_root = dummpy_child.next
        return root

