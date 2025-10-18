#MST以点为出发点的Prim算法
from collections import defaultdict
import heapq

def prim(n, edges):
    #先构造图
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append([v,w])
        graph[v].append([u,w])

    #构造heap和visited
    visited = set()
    heap = [(0,0)]
    total = 0
    while heap:
        cur_w, cur_node = heapq.heappop(heap)
        if cur_node in visited:
            continue
        visited.add(cur_node)
        for nei, nw in graph[cur_node]:
            if nei not in visited:
                heapq.heappush(heap, (nw, nei))
                total += nw

    return total