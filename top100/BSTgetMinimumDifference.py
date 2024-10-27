# 530
# BST节点的最小差值
# 中序遍历整个数，一直维护一个最小值，遍历完成后返回
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        prev = None
        min_diff = float("inf")
        #递归来中序遍历
        def inorder(root):
            nonlocal prev, min_diff
            if not root:
                return
            #左
            if root.left:
                inorder(root.left)
            #root
            if prev:
                min_diff = min(min_diff, abs(root.val - prev.val))
            prev = root

            #right
            if root.right:
                inorder(root.right)

        inorder(root)
        return min_diff

if __name__ == '__main__':
    s = Solution()
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.right.left = TreeNode(5)
    print(s.getMinimumDifference(tree))
