#dijkstra单源最短路径算法
#1.维护一个dist表示从start到目标的位置，一直维护目前的最小距离
#2.维护一个heap，来记录目前到所有node中的最小node，用它来进行下一步松弛操作

import heapq

def dijkstra(n, edges, start):
    #1.构件图
    graph = [[] for _ in range(edges)]
    for u,v,w in edges:
        graph[u].append([v, w])

    #构建dist
    INF = float("inf")
    dist = [INF]*n
    dist[start] = 0

    #构建heap
    heap = [(0, start)]

    #开始dijkstra
    while heap:
        cur_d, cur_node = heapq.heappop(heap)
        if cur_d >= dist[cur_node]:
            continue

        for u,w in graph[cur_node]:
            if dist[u] > dist[cur_node] + w:
                dist[u] = dist[cur_node] + w
                heapq.heappush(heap, (dist[u], u))
    return dist