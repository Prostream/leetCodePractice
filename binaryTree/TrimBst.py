#669 修建二叉搜索树
class Solution:
    def trimBST(self,root,low,high):
        if not root:
            return None
        if root.val < low:
            return self.trimBST(root.right,low,high)
        if root.val > high:
            return self.trimBST(root.left,low,high)
        root.left = self.trimBST(root.left,low,high)
        root.right = self.trimBST(root.right,low,high)
        return root

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

if __name__ == '__main__':
    #         4
    #        / \
    #       2   7
    #      / \ /
    #     1   3 3
    s = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(20)
    root.right.left = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    print(s.trimBST(root, 5,8))