#98 验证搜索二叉树
#方法1：中序遍历一直升序，说明是搜索二叉树
#方法2：递归的判断，左右子树是不是搜索二叉树，然后lmax<自己<rmin
class Solution(object):
    min_value = float('inf')
    max_value = float('-inf')
    def isValidBST(self, root):
        if root is None:
            self.min_value = float('inf')
            self.max_value = float('-inf')
            return True
        else:
            lok = self.isValidBST(root.left)
            lmin = self.min_value
            lmax = self.max_value
            rok = self.isValidBST(root.right)
            rmin = self.min_value
            rmax = self.max_value
            self.min_value = min(min(lmin,rmin), root.val)
            self.max_value = max(max(lmax,rmax), root.val)
            return lok and rok and lmax < root.val < rmin

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == '__main__':
    #         3
    #        / \
    #       9   20
    #          /  \
    #         15   7
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(s.isValidBST(root))