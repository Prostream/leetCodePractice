#112
#判断给定的二叉树中是否存在从根节点到叶子节点的路径，其路径上的节点值之和等于给定的目标和 targetSum。
#DFS or 递归
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        if root.left is None and root.right is None:
            if targetSum == root.val:
                return True
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)