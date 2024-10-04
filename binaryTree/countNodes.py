#222 Count Complete Tree Nodes
#思路：两种情况：
#1.如果右子树能扎到最下面一层，说明右子树是完全二叉树，递归右子树
#2，如果右子树不能扎到最下面一层，说明左子树是完全二叉树，递归左子树
class Solution:
    def countNodes(self, root):
        #这颗树的总层高
        dept = self.mostleft(root)
        nodes = self.f(root, dept)
        return nodes

    #计算完全二叉树的节点个数
    def f(self, root, dept):
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 1
        #如果右边能扎到最深层,说明右边
        n = self.mostleft(root)
        if root.right and self.mostleft(root.right) == n - 1:
            return 2**(n-1)+self.f(root.right, dept)
        # 如果右边不能扎到最深层,说明左边是完全二叉树
        if root.left and self.mostleft(root.right) == n - 2:
            return 2**(n-2)+self.f(root.left, dept)

    #计算一直走左子树能够扎到第几层
    def mostleft(self, root):
        dept = 1
        if root == None:
            return 0
        while root.left != None:
            dept = dept + 1
            root = root.left
        return dept

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

if __name__ == '__main__':
    #         3
    #        / \
    #       9   20
    #      / \ /
    #     1   2 3
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    print(s.countNodes(root))