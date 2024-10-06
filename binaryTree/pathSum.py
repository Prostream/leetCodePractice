#113
#二叉树里找到和为目标和的路径（root-leaf）
class Solution:
    def pathSum(self, root, targetSum):
        if not root:
            return []
        ans = []
        path = []
        cur_sum = 0
        self.f(root, cur_sum, targetSum, path, ans)
        return ans

    def f(self, root, cur_sum, targetSum, path, ans):
        if root.left is None and root.right is None:
            #找到路径
            if cur_sum + root.val == targetSum:
                path.append(root.val)
                ans.append(list(path))
                path.pop()
                return
        else:
            #不是叶节点
            cur_sum = root.val + cur_sum
            path.append(root.val)
            if root.left is not None:
                self.f(root.left, cur_sum, targetSum, path, ans)
            if root.right is not None:
                self.f(root.right, cur_sum, targetSum, path, ans)
            path.pop()
            return



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
    print(s.pathSum(root,30))