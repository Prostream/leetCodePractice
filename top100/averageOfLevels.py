# Definition for a binary tree node.
#计算二叉树中每一层节点值的平均值，并以列表的形式返回。
#用BFS
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        queue = deque()
        queue.append((root, 0))  # 节点和层数
        level_node_counts = []  # 每层节点的数量
        level_sum = []  # 每层节点值的总和

        while queue:
            cur_node, level = queue.popleft()
            if cur_node.left:
                queue.append((cur_node.left, level + 1))
            if cur_node.right:
                queue.append((cur_node.right, level + 1))

            if len(level_node_counts) < level + 1:
                # 初始化每一层的总和和节点数量
                level_node_counts.append(1)
                level_sum.append(cur_node.val)
            else:
                # 累加节点数量和节点值
                level_node_counts[level] += 1
                level_sum[level] += cur_node.val

        # 计算每层的平均值
        return [level_total / count for level_total, count in zip(level_sum, level_node_counts)]

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().averageOfLevels(root))
