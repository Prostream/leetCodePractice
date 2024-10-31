#983
#动态规划问题
from cmath import inf
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [inf] * (len(days)+1)
        return self.f3(days, costs, dp)


    # 递归法
    def f1(self, days, costs, i):
        duration = [1, 7, 30]
        if i == len(days):
            return 0
        ans = 100000000
        for plan in range(0, 3):
            j = i
            while j < len(days) and days[i] + duration[plan] > days[j]:
                j = j + 1
            ans = min(ans, costs[plan] + self.f1(days, costs, j))
        return ans


    # 记忆化搜索
    def f2(self, days, costs, i, dp):
        duration = [1, 7, 30]
        if i == len(days):
            return 0
        if dp[i] != -1:
            return dp[i]
        ans = 1000000000000
        for plan in range(0, 3):
            j = i
            while j < len(days) and days[i] + duration[plan] > days[j]:
                j = j + 1
            ans = min(ans, costs[plan] + self.f2(days, costs, j, dp))
        dp[i] = ans
        return ans

    # 从底到顶
    def f3(self, days, costs, dp):
        n = len(days)
        duration = [1, 7, 30]
        dp[n] =  0
        for i in range(len(days)-1,-1,-1):
            for plan in range(0, 3):
                j = i
                while j < len(days) and days[i] + duration[plan] > days[j]:
                    j = j + 1
                #print(f"i = {i} and j = {j}")  # 打印接收到的参数
                dp[i] = min(dp[i], costs[plan] + dp[j])

        return dp[0]

