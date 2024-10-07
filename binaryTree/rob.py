#337 rob 二叉树打家劫舍问题
#yes-这个树在偷头节点的情况下的最好收益 no-这个树在不偷头节点的情况下最好收益
class Solution:
    yes = 0
    no = 0
    def rob(self, root):
        self.f(root)
        return max(self.yes, self.no)

    def f(self, root):
        if root is None:
            self.yes = 0
            self.no = 0
            return
        else:
            cur_yes = root.val
            cur_no = 0
            self.f(root.left)
            cur_yes = cur_yes + self.no
            cur_no = cur_no + max(self.yes, self.no)
            self.f(root.right)
            cur_yes = cur_yes + self.no
            cur_no = cur_no + max(self.yes, self.no)
            self.yes = cur_yes
            self.no = cur_no
            return


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
    print(s.rob(root))