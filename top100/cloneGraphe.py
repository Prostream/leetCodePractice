from collections import deque
# 133 克隆图
# 类似随机指针链表的深拷贝，用一个hashmap存储新旧节点的对应关系，第二次遍历把邻居关系再带上
from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new_node = {}  # 映射原节点到克隆节点
        queue = deque([node])

        # 克隆第一个节点并存储
        old_to_new_node[node] = Node(node.val)

        while queue:
            cur_node = queue.popleft()

            # 遍历当前节点的所有邻居
            for neighbor in cur_node.neighbors:
                if neighbor not in old_to_new_node:
                    # 如果邻居没有被克隆，克隆邻居节点并加入队列
                    old_to_new_node[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                # 将克隆的邻居添加到当前克隆节点的邻居列表
                old_to_new_node[cur_node].neighbors.append(old_to_new_node[neighbor])

        # 返回克隆图的头部
        return old_to_new_node[node]

if __name__ == '__main__':
    s = Solution()
    print(s.cloneGraph(Node(1, [Node(2, [Node(4, [])]), Node(3, [])])))