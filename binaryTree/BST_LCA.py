#235-二叉搜索树的LCA
#从root往下
#1.遇到p，p就是答案
#2.遇到q，q就是答案
#3.如果root的值，在p，q之间，root是答案
#4.如果root的值在（p,q）左侧，右移root
#5.如果root的值在（p,q）右侧，左移root
class Solution:
    def lowestCommonAncestor(self,root,p,q):
        if root is None:
            return None
        while root.val != p and root.val != q:
            if min(q.val, p.val) < root.val < max(q.val, p.val):
                return root
            #右侧左移
            if max(q.val, p.val) < root.val:
                root = root.left
            #左侧右移
            if root.val < min(q.val, p.val):
                root = root.right
        return root

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

if __name__ == '__main__':
    #         6
    #        / \
    #       4    8
    #      / \  /
    #     3   5 7
    s = Solution()
    root = TreeNode(6)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.right.left = TreeNode(3)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(7)
    print(s.lowestCommonAncestor(root, root.left.left, root.right).val)