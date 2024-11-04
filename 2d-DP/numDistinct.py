#115
#一个s字符串的子序列，有多少个个t字符串完全一致
#dp[i,j]i表示前缀长度i的s部分，里有多少个可能和t的前缀长度j完全一致
#状态转移，如果i长度[0...i-1]的最后一位和[0...j-1]最后一位一致，说明可以变成1+dp[i-1][j-1]
#         如果不一致，就是dp[i-1][j]
#边界条件：i=0 说明只有空集，
from collections import defaultdict


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = defaultdict(int)

        # 记忆化搜索
        def f1(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            # 边界条件，j==0说明t的空集部分，任何情况都会有1个和它完全一致
            if j == 0:
                dp[(i, j)] = 1
                return dp[(i, j)]
            if i == 0 and j != 0:
                dp[(i, j)] = 0
                return dp[(i, j)]
            dp[(i, j)] = f1(i - 1, j)
            if s[i - 1] == t[j - 1]:
                dp[(i, j)] = f1(i - 1, j - 1) + dp[(i, j)]
            return dp[(i, j)]

        # 自底向上，需要的是左上和上
        def f2():
            # 先处理好边边角角
            for j in range(1, len(t) + 1):
                dp[(0, j)] = 0
            for i in range(0, len(s) + 1):
                dp[(i, 0)] = 1
            for i in range(1, len(s) + 1):
                for j in range(1, len(t) + 1):
                    dp[(i, j)] = dp[(i - 1, j)]
                    if s[i - 1] == t[j - 1]:
                        dp[(i, j)] = dp[(i - 1, j - 1)] + dp[(i, j)]
            return dp[(len(s), len(t))]

        # 空间压缩
        def f3():
            dprow = [0] * (len(t) + 1)
            for i in range(len(s) + 1):
                if i == 0:
                    for j in range(len(t), -1, -1):
                        dprow[j] = 0
                        dprow[0] = 1
                else:
                    for j in range(len(t), -1, -1):
                        if j == 0:
                            dprow[j] = 1
                            continue
                        dprow[j] = dprow[j]
                        if s[i - 1] == t[j - 1]:
                            dprow[j] = dprow[j - 1] + dprow[j]
                # print(f"dp={dprow}")

            return dprow[len(t)]

        # return f1(len(s),len(t))
        return f3()
