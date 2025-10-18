from collections import defaultdict
import heapq
#求A-B的最短路径，直接使用dijkstra最短路径算法
def getShortestRoute(roads_nodes, roads_from, roads_to, roads_weight, a, b):
    n = roads_nodes
    #先构建图
    graph = defaultdict(list)
    for u,v,w in zip(roads_from, roads_to, roads_weight):
        graph[u].append([v,w])
        graph[v].append([u,w])

    #构建dist
    INF = float("inf")
    dist = [INF]*n
    dist[a] = 0

    #准备heap 前面是val后面是node
    heap = [(0,a)]

    while heap:
        cur_w, cur_n = heapq.heappop(heap)
        if cur_w > dist[cur_n]:
            continue
        #松弛操作
        for nei, nw in graph[cur_n]:
            if dist[nei] > nw + dist[cur_n]:
                dist[nei] = nw + dist[cur_n]
                heapq.heappush(heap, (dist[nei], nei))
    return dist[b]

if __name__ == '__main__':
    roads_nodes = 4
    roads_from = [0,1,2,3]
    roads_to = [1,2,3,0]
    roads_weight = [1,2,3,4]
    a = 1
    b = 3
    print(getShortestRoute(roads_nodes, roads_from, roads_to, roads_weight, a, b))
