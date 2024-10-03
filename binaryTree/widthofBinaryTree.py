#leetcode-662
#左子节点的编号2i，右子节点的编号2i+1
#维护两个队列，同步进退，分别放置节点本身和编号
class Solution:
    def widthOfBinaryTree(self, root):
        l=r=0
        maxamount = 1
        queueofNode = [root]
        r = r + 1
        queueofIndex = [1]#第一个节点当1
        while l < r:
            maxamount = max(maxamount, queueofIndex[r-1] - queueofIndex[l] + 1 )
            size = r - l
            for i in range(size):
                curNode = queueofNode[l]
                curIndex = queueofIndex[l]
                l = l + 1
                if curNode.left is not None:
                    queueofNode.append(curNode.left)
                    queueofIndex.append(curIndex*2)
                    r = r + 1
                if curNode.right is not None:
                    queueofNode.append(curNode.right)
                    queueofIndex.append(curIndex*2 + 1)
                    r = r + 1
        return maxamount

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
    print(s.widthOfBinaryTree(root))

