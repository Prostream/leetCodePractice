#879
#3维01背包问题，
#n是人员数量，minProfit是最低要达到的利润，group是ith工作需要的人员，profit是每个工作对应的利润,一共有多少种方式
#递归dp(i,r,s)i是[i...n-1]个工作，r是剩下的人，s剩下要达成的profit
import functools
from typing import List


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod = 1000000007

        # 暴力递归
        @functools.cache
        def f0(i, r, s):
            if i >= len(group):  # 没工作可选了
                return 1 if s <= 0 else 0
            if r <= 0:  # 没人可用了
                return 1 if s <= 0 else 0

            # 不做当前这个i工作
            p1 = f0(i + 1, r, s)
            # 做当前这个i工作(满足条件下)
            p2 = 0
            if group[i] <= r:  # 人员够
                p2 = f0(i + 1, r - group[i], s - profit[i])
            return (p1 + p2) % mod

        # 记忆化搜索
        dp = defaultdict(int)

        def f1(i, r, s):
            # print(f"i={i} r={r} s={s}")
            if (i, r, s) in dp:
                return dp[(i, r, s)]
            if i >= len(group):  # 没工作可选了
                dp[(i, r, s)] = 1 if s <= 0 else 0
                return dp[(i, r, s)]
            if r <= 0:  # 没人可用了
                dp[(i, r, s)] = 1 if s <= 0 else 0
                return dp[(i, r, s)]

            # 不做当前这个i工作
            p1 = f1(i + 1, r, s)
            # 做当前这个i工作(满足条件下)
            p2 = 0
            if group[i] <= r:  # 人员够
                p2 = f1(i + 1, r - group[i], max(0, s - profit[i]))
            dp[(i, r, s)] = (p1 + p2) % mod
            return dp[(i, r, s)]

        # 记忆化搜索
        dp = [[[-1 for s in range(minProfit + 1)] for r in range(n + 1)] for i in range(len(group) + 1)]

        def f4(i, r, s):
            # print(f"i={i} r={r} s={s}")
            if dp[i][r][s] != -1:
                return dp[i][r][s]
            if i >= len(group):  # 没工作可选了
                dp[i][r][s] = 1 if s <= 0 else 0
                return dp[i][r][s]
            if r <= 0:  # 没人可用了
                dp[i][r][s] = 1 if s <= 0 else 0
                return dp[i][r][s]

            # 不做当前这个i工作
            p1 = f4(i + 1, r, s)
            # 做当前这个i工作(满足条件下)
            p2 = 0
            if group[i] <= r:  # 人员够
                p2 = f4(i + 1, r - group[i], max(0, s - profit[i]))
            dp[i][r][s] = (p1 + p2) % mod
            return dp[i][r][s]

        # 空间压缩
        # def f1

        # return f0(0,n,minProfit)
        # return f1(0,n,minProfit)
        return f4(0, n, minProfit)