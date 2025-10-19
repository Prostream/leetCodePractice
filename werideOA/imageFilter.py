#第 i 张图片在区间 [startDay[i], endDay[i]] 的每一天都需要处理，单日费用为 filterCost[i]。
#
#当天的总费用 = 所有“当日活跃图片”的费用和；但可以用日折扣价 discountPrice 作为封顶价：
#dayCost = min( sumActive, discountPrice )
#
#目标：把所有天的费用加总并取模。
from collections import defaultdict

MOD = 10**7+9
def getMinProcessingCost(filterCost, startDay, endDay, discountPrice):
    event = defaultdict(int)
    n = len(filterCost)
    for i in range(n):
        event[startDay[i]] += filterCost[i]
        event[endDay[i] + 1] -= filterCost[i]

    ans = 0
    prev_day = None
    runningCost = 0
    days = sorted(event.keys())
    for day in days:
        if prev_day is not None:
            cost = min(discountPrice, runningCost)
            length = day - prev_day
            ans = (ans + cost * length)%MOD
        prev_day = day
        runningCost += event[day]
    return ans

if __name__ == "__main__":
    n = 3
    filterCost = [2, 3, 4]
    startDay = [1, 1, 2]
    endDay = [2, 3, 4]
    discountPrice = 6

    ans = getMinProcessingCost(filterCost, startDay, endDay, discountPrice)
    print(ans)  # 期望输出 21