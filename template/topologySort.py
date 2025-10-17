from collections import defaultdict
from collections import deque
def topological_sort(n, edges):
    #先构建图
    graph = defaultdict(list)
    for u,v in edges:
        graph[v].append(u)

    #准indegree队列
    indgree = [0]*n
    for v in graph:
        for nei in graph[v]:
            indgree[nei] += 1
    queue = deque()
    for i in range(n):
        if indgree[i] == 0:
            queue.append(i)

    topo = []
    #遍历队列，开始拓扑排序
    while queue:
        cur = queue.popleft()
        topo.append(cur)
        for nei in graph[cur]:
            indgree[nei] -= 1
            if indgree[nei] == 0:
                queue.append(nei)
    if len(topo) < n:
        return False#有环

    return True #无环