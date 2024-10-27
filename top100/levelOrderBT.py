# 102 二叉树层序遍历，其实就是BFS，队列
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        ans = []
        queue = deque()
        level = 0
        queue.append((root,level))
        while queue:
            cur = queue.popleft()
            if cur.left:
                queue.append((cur.left, level+1))
                level += 1
            if cur.right:
                queue.append(cur.right)
            ans.append(cur.val)
        return ans