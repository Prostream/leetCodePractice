#101 对称树
#左右一起数吧
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def left_traverse(path, root):
            if root is None:
                return path.append("Null")
            #pre-order
            path.append(root.val)
            path.append("Null" if root.left is None else root.left.val)
            path.append("Null" if root.right is None else root.right.val)
            left_traverse(path, root.left)
            left_traverse(path, root.right)

        def right_traverse(path, root):
            if root is None:
                return path.append("Null")
            #pre-order 先右后左
            path.append(root.val)
            path.append("Null" if root.right is None else root.right.val)
            path.append("Null" if root.left is None else root.left.val)
            right_traverse(path, root.right)
            right_traverse(path, root.left)

        path_left = []
        path_right = []
        left_traverse(path_left, root.left)
        right_traverse(path_right, root.right)

        if len(path_left) != len(path_right):
            return False
        for l, r in zip(path_left, path_right):
            if l != r:
                return False
        return True

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(3)
    print(Solution().isSymmetric(root))