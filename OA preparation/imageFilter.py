def getMinProcessingCost(filterCost, startDay, endDay, discountPrice):
    """
    :param filterCost: List[int], 第 i 张图像的单日处理费用
    :param startDay:   List[int], 第 i 张图像开始处理的日期
    :param endDay:     List[int], 第 i 张图像结束处理的日期（含）
    :param discountPrice: int, 当天对所有图像统一处理时的折扣总价
    :return: int, 最小总费用 % (10^9 + 7)
    """
    import sys
    from collections import defaultdict

    MOD = 10 ** 9 + 7
    n = len(filterCost)

    # 1) 收集事件：+cost 表示从该天起多了一张图要处理；-cost 表示该天起少了一张图要处理
    events = defaultdict(int)
    for i in range(n):
        events[startDay[i]] += filterCost[i]  # 开始日
        # “结束日+1”这天不再需要处理该图像
        # 注意要防止潜在溢出，Python int 无上限一般没问题，但若语言有限制需判一下 endDay[i]+1 是否越界
        events[endDay[i] + 1] -= filterCost[i]

    # 2) 将所有事件天按升序排好
    days = sorted(events.keys())

    total_cost = 0
    runningCost = 0  # 当前需要处理的图像费用总和
    prevDay = None  # 上一个事件日

    # 3) 线性扫描事件日
    for day in days:
        if prevDay is not None:
            # 区间 [prevDay, day) 这几天的费用相同
            length = day - prevDay
            # 对这段天数，每天付费可选 runningCost(逐图像) 或 discountPrice(打包价)
            dailyCost = min(runningCost, discountPrice)
            total_cost = (total_cost + dailyCost * length) % MOD

        # 更新本日的变动（某些图像开始或结束）
        runningCost += events[day]
        prevDay = day

    return total_cost % MOD


# 下面是题目给的示例测试:
if __name__ == "__main__":
    n = 3
    filterCost = [2, 3, 4]
    startDay = [1, 1, 2]
    endDay = [2, 3, 4]
    discountPrice = 6

    ans = getMinProcessingCost(filterCost, startDay, endDay, discountPrice)
    print(ans)  # 期望输出 21
