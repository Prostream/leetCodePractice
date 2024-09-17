#leetcode-134
#n个加油站，第i个加油站有g[i]升汽油
#i->i+1耗油cost[i]
#如果你可以按照顺序环绕路形式一周，返回出发时加油站的编号，否则返回-1
#思路很巧妙，余量数组，第一个导致无法走一圈的加油站前面出发的都无法走一圈从而优化了循环
def gas_station(gas, cost):
    #余量数组为 gas[i]-cost[i]
    left = 0
    right = 0
    #0 1 2 3 4 5 0 1 2 3 4 5 (12个)
    while left < len(gas):
        sum = 0
        while sum + gas[right%len(gas)] - cost[right%len(gas)] >= 0:
            sum = sum + gas[right%len(gas)] - cost[right%len(gas)]
            if right - left == len(gas) - 1:
                return left
            right = right + 1
        left = right + 1
        right = left
    return -1