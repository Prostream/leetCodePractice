#114
#一棵二叉树原地转换为一个单链表 前序遍历的方式 链表的next用right替代使用
# 左边flatten好，右边flatten好，把右边保存好，然后root.right=flatten好的左边。然后找到现在链表的最末尾，把右边加上
# 还可以使用morris法
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        right_tree = root.right
        root.right = root.left

        current = root
        while current.right:
            current = current.right
        #连上
        current.right = right_tree



