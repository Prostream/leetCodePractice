#399
#处理两个变量之间的除法关系 是双向有向图问题
#先构建一个双向图(什么形式？邻居数组)
#对于每一个query，看看能不能走到
#   能就算出结果
#   不能就返回-1
#能不能走到，需要用到dfs or bfs
#注意traverse的时候需要去重
from cgitb import reset
from collections import defaultdict
from itertools import product
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        #构建图
        graph = defaultdict(dict)
        for (v,u), value in zip(equations, values):
            graph[v][u] = value
            graph[u][v] = 1/value

        #dfs计算两点之间的路径成绩和
        def dfs(start, end, visited):
            if start == end:
                return 1.0
            if start not in graph or end not in graph:
                return -1.0
            visited.add(start)

            for neighbor in graph[start]:
                if neighbor in visited:
                    continue
                product = dfs(neighbor, end, visited)
                if product != -1.0:
                    return product * graph[start][neighbor]
            return -1.0

        # 对每个查询执行DFS
        results = []
        for num, den in queries:
            if num not in graph or den not in graph:
                results.append(-1.0)
            else:
                results.append(dfs(num, den, set()))

        return results