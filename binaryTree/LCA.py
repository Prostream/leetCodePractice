#236-查询两个节点的最低公共祖先
#巧妙的设置遍历方案，可以轻松解决
#1.包含关系
#2.分属于两棵树,谁同时拥有两棵树就是公共祖先
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root is None or root == p or root == q:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r:
            return root
        if l is None and r is None:
            return None
        return l if l is not None else r

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
    print(s.lowestCommonAncestor(root, root.left.left, root.right).val)