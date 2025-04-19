import bisect

def closestStraightCity(cityName, x, y, q):
    """
    :param cityName: List[str], 第 i 个城市的名字
    :param x:        List[int], 第 i 个城市的 x 坐标
    :param y:        List[int], 第 i 个城市的 y 坐标
    :param q:        List[str], 要查询的城市名字列表
    :return:         List[str], 对应每个查询城市的最近同 x 或同 y 城市名字；若无则 "NONE"
    """
    n = len(cityName)

    # 1) 建立 名字->下标 的映射
    nameToIndex = {}
    for i, nm in enumerate(cityName):
        nameToIndex[nm] = i

    # 2) 分组: xMap[x] = [(y_i, cityName_i, idx_i), ...] 按 y_i 升序
    #           yMap[y] = [(x_i, cityName_i, idx_i), ...] 按 x_i 升序
    from collections import defaultdict
    xMap = defaultdict(list)
    yMap = defaultdict(list)

    for i in range(n):
        xMap[x[i]].append((y[i], cityName[i], i))
        yMap[y[i]].append((x[i], cityName[i], i))

    # 对每个坐标把列表排好序
    for X in xMap:
        xMap[X].sort(key=lambda tup: tup[0])  # tup = (y, name, idx)
    for Y in yMap:
        yMap[Y].sort(key=lambda tup: tup[0])  # tup = (x, name, idx)

    # 帮助函数: 给定 (x0,y0) 和候选 idx，返回它们之间的 (距离, 名字)
    #           曼哈顿距离 = abs(x[idx] - x0) + abs(y[idx] - y0)
    def dist_info(i0, i1):
        d = abs(x[i1] - x[i0]) + abs(y[i1] - y[i0])
        return (d, cityName[i1])

    # 查找同 x 的最近候选
    def get_candidates_same_x(i0):
        X = x[i0]
        y0 = y[i0]
        arr = xMap[X]  # list of (y_val, name, idx)
        # 在 arr 里二分查找 y0 所在位置
        pos = bisect.bisect_left(arr, (y0, "", 0))
        cands = []
        # pos 左侧、右侧各可能有一个邻居
        if pos < len(arr):
            cands.append(arr[pos])
        if pos - 1 >= 0:
            cands.append(arr[pos - 1])
        if pos + 1 < len(arr):
            cands.append(arr[pos + 1])
        # 去重
        cands = list(set(cands))
        return [c[2] for c in cands]  # 返回 idx 列表

    # 查找同 y 的最近候选
    def get_candidates_same_y(i0):
        Y = y[i0]
        x0 = x[i0]
        arr = yMap[Y]  # list of (x_val, name, idx)
        pos = bisect.bisect_left(arr, (x0, "", 0))
        cands = []
        if pos < len(arr):
            cands.append(arr[pos])
        if pos - 1 >= 0:
            cands.append(arr[pos - 1])
        if pos + 1 < len(arr):
            cands.append(arr[pos + 1])
        cands = list(set(cands))
        return [c[2] for c in cands]

    # 3) 处理查询
    res = []
    for qName in q:
        i0 = nameToIndex[qName]
        cand_x = get_candidates_same_x(i0)
        cand_y = get_candidates_same_y(i0)
        all_cand = set(cand_x + cand_y)
        # 排除自己
        if i0 in all_cand:
            all_cand.remove(i0)
        if not all_cand:
            res.append("NONE")
            continue
        # 计算 (distance, name) 并取最小
        best = None
        for i1 in all_cand:
            cur = dist_info(i0, i1)  # (dist, cityName)
            if best is None or cur < best:
                best = cur
        # best = (dist, name)
        res.append(best[1])

    return res


# ============== 测试示例 ==============
if __name__ == "__main__":
    # 题目给的例子:
    # n=3
    # cityName = ["c1", "c2", "c3"]
    # x=[3,2,1], y=[3,2,3]
    # q=["c1","c2","c3"]
    # 期望输出: ["c3","NONE","c1"]
    cityName = ["c1", "c2", "c3"]
    x = [3, 2, 1]
    y = [3, 2, 3]
    queries = ["c1", "c2", "c3"]
    ans = closestStraightCity(cityName, x, y, queries)
    print(ans)  # ['c3', 'NONE', 'c1']
