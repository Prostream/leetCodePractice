import math


def connectedSum(graph_nodes, graph_from, graph_to):
    """
    graph_nodes: int, 节点总数(编号1..graph_nodes)
    graph_from, graph_to: List[int], 每条边的两个端点
    返回: sum of ceil(sqrt(size_of_component)) over all components
    """
    n = graph_nodes

    # 并查集
    parent = list(range(n + 1))  # 下标 1..n
    size = [1] * (n + 1)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

    # 读入边
    for u, v in zip(graph_from, graph_to):
        union(u, v)

    # 遍历所有根，计算各自集合大小
    visited_root = set()
    ans = 0
    for i in range(1, n + 1):
        r = find(i)
        if r not in visited_root:
            visited_root.add(r)
            comp_size = size[r]
            # ceil of sqrt
            sr = math.isqrt(comp_size)  # integer sqrt (floor)
            if sr * sr == comp_size:
                ans += sr
            else:
                ans += (sr + 1)

    return ans


# =============== 测试示例 ===============
if __name__ == "__main__":
    # 题目示例
    graph_nodes = 10
    graph_from = [1, 1, 2, 3, 7]
    graph_to = [2, 3, 4, 5, 8]
    # 预期输出 8
    print(connectedSum(graph_nodes, graph_from, graph_to))  # 8
