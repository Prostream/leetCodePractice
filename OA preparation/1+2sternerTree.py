import heapq
import math

def getShortestRoute(roads_nodes, m, a, b, c, roads_from, roads_to, roads_weight):
    # 1) 建立邻接表 graph[node] = [(nbr, w), ...]
    graph = [[] for _ in range(roads_nodes)]
    for i in range(m):
        u = roads_from[i]
        v = roads_to[i]
        w = roads_weight[i]
        graph[u].append((v, w))
        graph[v].append((u, w))

    # 2) 定义 Dijkstra 函数
    def dijkstra(start):
        dist = [math.inf]*roads_nodes
        dist[start] = 0
        minheap = [(0, start)]  # (距离, 节点)
        while minheap:
            cur_d, node = heapq.heappop(minheap)
            if cur_d > dist[node]:
                continue
            # 遍历相邻节点
            for (nbr, w) in graph[node]:
                new_d = cur_d + w
                if new_d < dist[nbr]:
                    dist[nbr] = new_d
                    heapq.heappush(minheap, (new_d, nbr))
        return dist

    # 3) 分别对 a, b, c 做 Dijkstra
    distA = dijkstra(a)
    distB = dijkstra(b)
    distC = dijkstra(c)

    # 4) 遍历所有节点 u，取 distA[u] + distB[u] + distC[u] 的最小值
    best = math.inf
    for u in range(roads_nodes):
        cost = distA[u] + distB[u] + distC[u]
        if cost < best:
            best = cost

    return best if best != math.inf else -1


# =============== 示例测试 ===============
if __name__ == "__main__":
    # 题目示例：
    # roads_nodes=4, m=3, a=1, b=3, c=2
    # edges: (0->2, w=1), (0->1, w=2), (0->3, w=3)
    roads_nodes = 4
    m = 3
    a, b, c = 1, 3, 2
    roads_from = [0, 0, 0]
    roads_to   = [2, 1, 3]
    roads_weight = [1, 2, 3]
    ans = getShortestRoute(roads_nodes, m, a, b, c, roads_from, roads_to, roads_weight)
    print(ans)  # 期望输出: 6 (示例给出的最短路径代价)
