#129
#要求计算从根节点到叶子节点的所有路径组成的数字之和。
# DFS找到一个叶子节点就加一次
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def nodeSum(current, sum):
            if not current:
                return 0
            if not current.left and not current.right:
                return sum*10 + current.val

            sum = sum*10 + current.val
            return nodeSum(current.left, sum) + nodeSum(current.right, sum)

        return nodeSum(root, 0)