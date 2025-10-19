from collections import defaultdict


def compute_distance_metrics(arr):
    n = len(arr)
    res = [0] * n
    groups = defaultdict(list)

    # 将相同值的下标收集到一起
    for i, v in enumerate(arr):
        groups[v].append(i)

    for pos in groups.values():
        pos.sort()  # 排序，保证下标从小到大
        m = len(pos)
        # 构造前缀和数组: prefix[i] 表示 pos[0] + ... + pos[i-1]
        prefix = [0]
        for p in pos:
            prefix.append(prefix[-1] + p)

        # 对于每个位置 pos[k]，计算左侧和右侧贡献
        for k, p in enumerate(pos):
            left = k * p - prefix[k]
            right = (prefix[m] - prefix[k + 1]) - (m - 1 - k) * p
            res[p] = left + right

    return res


# ============== 测试 ==============
if __name__ == "__main__":
    arr = [1, 2, 1, 1, 2, 3]
    # 期望输出: [5, 3, 3, 4, 3, 0]
    # map {[1:0,2,3], [2:1,4], [3:5]}
    # pre {[x:0,2,5], [x:1,5], [x:5]}
    print(compute_distance_metrics(arr))
