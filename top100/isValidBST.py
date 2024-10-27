# 98题 判断是不是一个BST
# 递归，判断下自己的满足 left<=root<=right吗，再看看左右子树满足不, 如果没有左右子树，算满足(这个思路可能出现问题，左子树的右子树有孙子大于爷爷的可能)
# 需要每次递归的时候带着边界
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isBST(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True

            # 当前节点的值必须在 low 和 high 之间
            if node.val <= low or node.val >= high:
                return False

            # 递归检查左右子树，更新区间范围
            return isBST(node.left, low, node.val) and isBST(node.right, node.val, high)

        return isBST(root)