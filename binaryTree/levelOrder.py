#leetcode-102
#二叉树的层序遍历
#数组实现队列
#1.取得队列的size
#2.执行（队列.弹出，子节点入队列）size次，放进答案
class Solution(object):
    def levelOrder(self, root):
        ans = []

        l = 0
        r = 0
        thisqueue = []
        thisqueue.append(root)
        r = r + 1
        #队列里还有东西
        while l < r :
            size = r - l
            level = []
            for i in range(size):
                #queue.pop()
                cur = thisqueue[l]
                l = l + 1
                if cur is not None:
                    level.append(cur.val)
                    if cur.left is not None:
                        thisqueue.append(cur.left)
                        r = r + 1
                    if cur.right is not None:
                        thisqueue.append(cur.right)
                        r = r + 1
            if len(level) >= 1:
                ans.append(level)
        return ans

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
    print(s.levelOrder(root))