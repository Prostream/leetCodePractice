#199题
#二叉树的右视图
# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        queue = deque()
        ans = []
        queue.append((root, 1))#节点，第几层
        not_change_level = 0
        last_node_val = 0
        while queue:
            cur_node, level = queue.popleft()#当前节点和现在是第几层
            if cur_node.left:
                queue.append((cur_node.left, level + 1))
            if cur_node.right:
                queue.append((cur_node.right, level + 1))
            #换行了
            if level == not_change_level+1:
                not_change_level += 1
                ans.append(last_node_val)
            last_node_val = cur_node.val
        ans.append(last_node_val)
        return ans[1:]

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(5)
    root.right.right = TreeNode(4)
    print(Solution().rightSideView(root))