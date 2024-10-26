from collections import deque


#116 完美二叉树每层连起来
# 层序遍历
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
        queue = deque() #数组来实现队列是O(N) deque是O(1
        queue.append(root)
        while queue:
            cur_root = queue.popleft()
            #把子节点连起来
            if cur_root.left and cur_root.right:
                cur_root.left.next = cur_root.right
                if cur_root.next is not None:
                    cur_root.right.next = cur_root.next.left
                queue.append(cur_root.left)
                queue.append(cur_root.right)
        return root

