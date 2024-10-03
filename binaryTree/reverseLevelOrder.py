#leetcode-103
#锯齿形层序遍历，同样利用queue
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        l=r=0
        ans = []
        #用l和r控制，python的list是动态的本身弹出头部的时间复杂度不行
        queue=[root]
        r = r + 1
        #队列里还有数
        reverse = False
        level = []
        while l < r:
            size = r -l
            #reverse=True 从右往左
            if not reverse:
                #从l到r-1
                for i in range(l,r):
                    level.append(queue[i].val)
            if reverse:
                #从l到r-1
                for i in range(r-1,l-1,-1):
                    level.append(queue[i].val)
            #reverse=False 从左往右

            for i in range(size):
                cur = queue[l]
                l = l + 1
                if cur.left is not None:
                    queue.append(cur.left)
                    r = r + 1
                if cur.right is not None:
                    queue.append(cur.right)
                    r = r + 1
            reverse = not reverse
            ans.append(level)
            level = []
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
    print(s.zigzagLevelOrder(root))