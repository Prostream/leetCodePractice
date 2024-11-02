#91题，经典的decode
#
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}

        #暴力尝试
        def f0(i):
            # 越界的时候返回1，代表之前的决策终于完成了
            if i == len(s):
                return 1
            if int(s[i]) == 0:
                return 0
            # "1"->A
            count = f(i + 1)
            if int(s[i] + s[i + 1]) <= 26:
                count = count + f(i + 2)
            return count

        # [i.....]能有几个decode way
        def f(i):
            if i in dp:
                return dp[i]
            else:
                # 转不了
                # 越界的时候返回1，代表之前的决策终于完成了
                if i == len(s):
                    dp[i] = 1
                    return 1
                if int(s[i]) == 0:
                    dp[i] = 0
                    return 0
                # 转1位
                if i == len(s) - 1:
                    dp[i] = 1
                    return 1
                # "1"->A
                count = f(i + 1)
                if int(s[i] + s[i + 1]) <= 26:
                    count = count + f(i + 2)
                dp[i] = count
                return count

        # 从底到顶
        def f2():
            n = len(s)
            dp[n] = 1
            for i in range(n - 1, -1, -1):
                if s[i] == '0':
                    dp[i] = 0
                else:
                    count = dp[i + 1]
                    # print(f"i={i}")
                    if i + 1 < n and int(s[i] + s[i + 1]) <= 26:
                        count = count + dp[i + 2]
                    dp[i] = count
            return dp[0]

        return f(0)