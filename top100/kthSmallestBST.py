# 230
# 取得BST里第k个最小元素，中序遍历，第k个元素就是第k个最小元素
# 中序遍历BST，维护一个count，如果count==k（生成一个数后）
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = None
        def inorder(root):
            nonlocal count, result
            if not root or result:
                return
            if root.left:
                inorder(root.left)
            #处理自己
            count += 1
            if count == k:
                result = root.val
                return result

            if root.right:
                inorder(root.right)

        inorder(root)
        return result