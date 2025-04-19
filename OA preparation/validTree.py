def maxValidConnections(n, from_nodes, to_nodes, cost, value):
    """
    n:          节点总数 (0..n-1)
    from_nodes: 长度 n-1, 表示边的父节点
    to_nodes:   长度 n-1, 表示边的子节点
    cost:       长度 n-1, cost[i] 是 (from_nodes[i] -> to_nodes[i]) 的费用
    value:      长度 n,   value[i] 是节点 i 的取值
    返回: 满足题意的有效连接数。
    """
    import sys
    sys.setrecursionlimit(10**7)

    # 1) 找到根 (入度为 0 的节点)
    in_degree = [0]*n
    for c in to_nodes:
        in_degree[c] += 1
    # 题目保证是一棵有向树，必有且仅有一个根
    root = next(i for i in range(n) if in_degree[i] == 0)

    # 2) 建立邻接表: graph[u] = [(child, cost_uv), ...]
    graph = [[] for _ in range(n)]
    for i in range(len(from_nodes)):
        u = from_nodes[i]
        v = to_nodes[i]
        w = cost[i]
        graph[u].append((v, w))

    # 3) DFS 计算深度 & 统计有效连接
    ans = 0
    def dfs(u, depth_u):
        nonlocal ans
        for (v, w) in graph[u]:
            depth_v = depth_u + 1
            # 如果该边费用 < value[v]，则 v 与其所有祖先均能形成有效连接
            if w < value[v]:
                ans += depth_v  # 因为v有depth_v个祖先(深度=depth_v)

            dfs(v, depth_v)

    dfs(root, 0)
    return ans


# ============ 测试一下 =============
if __name__ == "__main__":
    # 构造一个简单示例:
    #  节点: 0(根),1,2,3
    #  边: 0->1(cost=5), 0->2(cost=3), 2->3(cost=4)
    #  value=[2,10,10,5]
    #
    #  root=0, depth[0]=0
    #    child=1: cost=5 < value[1]=10 => ans+=depth[1]=1
    #    child=2: cost=3 < value[2]=10 => ans+=depth[2]=1
    #       child=3: cost=4 < value[3]=5 => ans+=depth[3]=2
    #
    #  总计 ans=1+1+2=4
    n = 4
    from_nodes = [0, 0, 2]
    to_nodes   = [1, 2, 3]
    cost       = [5, 3, 4]
    value      = [2, 10, 10, 5]

    print(maxValidConnections(n, from_nodes, to_nodes, cost, value))
    # 期望输出: 4
