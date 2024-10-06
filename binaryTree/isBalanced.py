#110 平衡二叉树
#给一个树，判断是否平衡（每个节点都满足，左右子树高度差不大于1）

class Solution(object):
    balance = True

    def isBalanced(self, root):
        if not root:
            return True
        self.height(root)
        return self.balance

    def height(self, root):
        if not root:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        if abs(lh - rh) > 1:
            self.balance = False
            return 0
        return 1 + max(lh, rh)


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(s.zigzagLevelOrder(root))