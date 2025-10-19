def final_prices(price, queries):
    n = len(price)
    res = [None]*n       # 最终答案
    set_flag = [False]*n # 是否已确定最终值

    floorv = -10**30

    # 倒序处理
    for tp, a, b in reversed(queries):
        if tp == 2:
            v = a  # 题目示例中写成 [2, v, v]，第二个参数也是 v，无需理会
            floorv = max(floorv, v)
        else:  # tp == 1
            x, v = a-1, b        # 若输入是 1-index
            if not set_flag[x]:
                res[x] = max(v, floorv)
                set_flag[x] = True

    # 未被确定的位置用 max(初值, floor)
    for i in range(n):
        if not set_flag[i]:
            res[i] = max(price[i], floorv)
    return res

# 例子
# n=3, price=[7,5,4]
# queries = [[2,6,6],[1,2,9],[2,8,8]] -> [8,9,8]