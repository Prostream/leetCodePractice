#207
#选课题，拓扑排序, [[0,1],[2,3]]
#拓扑排序，先建立入度表，然后一个个取掉节点，用队列+循环len次挺合适的
from collections import deque, defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #入度表
        in_degree = [0] * numCourses
        graph = defaultdict(list)

        # 构建图和计算每个节点的入度
        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1

        # 入度为0的节点入队
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        visited_count = 0

        # 进行拓扑排序
        while queue:
            node = queue.popleft()
            visited_count += 1
            # 遍历当前节点的所有邻接节点
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # 如果访问的节点数等于课程数，说明没有环
        return visited_count == numCourses
