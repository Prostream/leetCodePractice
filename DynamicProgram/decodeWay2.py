#带着*的decode，讨论变得比较复杂
"""
1.i为0，0种
2.一位编码，调用dp(i+1)，
   1.为数字，1种，1*dp(i+1)
   2.为*，9种，9*dp(i+1)
3，二位编码，调用dp(i+2)
   1.num，num
        1.1 如果num num > 26 0
        1.2 如果num num <= 26 1
   2.* num
        2.1 如果num在[7-9]，*=1 1种
        2.2 如果num在[1-6]，*=1or2 2种
   3.num *
        3.1 如果num=1，11-19 9种
        3.2 如果num=2，21-26 6种
        3.3 如果num > 2, 0种
   4.* * 15种
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}

        # 暴力
        def f0(i):
            count = 0
            if i == len(s):
                return 1
            #
            if s[i] == '0':
                return 0
            # 2
            if s[i] == '*':
                count += 9 * f0(i + 1)
            else:
                count += 1 * f0(i + 1)
            # 3.1
            if i + 1 <= len(s) - 1:
                if s[i] != '*' and s[i + 1] != '*':
                    if int(s[i] + s[i + 1]) > 26:
                        count += 0
                    else:
                        count += 1 * f0(i + 2)
                # 3.2
                elif s[i] == '*' and s[i + 1] != '*':
                    if s[i + 1] in ['7', '8', '9']:
                        count += 1 * f0(i + 2)
                    else:
                        count += 2 * f0(i + 2)
                # 3.3
                elif s[i] != '*' and s[i + 1] == '*':
                    if s[i] == '1':
                        count += 9 * f0(i + 2)
                    elif s[i] == '2':
                        count += 6 * f0(i + 2)
                    else:
                        count += 0
                elif s[i] == '*' and s[i + 1] == '*':
                    count += 15 * f0(i + 2)
            return count

        # 记忆化搜索
        def f1(i):
            if i in dp:
                return dp[i]
            count = 0
            if i == len(s):
                dp[i] = 1
                return 1
            #
            if s[i] == '0':
                dp[i] = 0
                return 0
            # 2
            if s[i] == '*':
                count += 9 * f1(i + 1)
            else:
                count += 1 * f1(i + 1)
            # 3.1
            if i + 1 <= len(s) - 1:
                if s[i] != '*' and s[i + 1] != '*':
                    if int(s[i] + s[i + 1]) > 26:
                        count += 0
                    else:
                        count += 1 * f1(i + 2)
                # 3.2
                elif s[i] == '*' and s[i + 1] != '*':
                    if s[i + 1] in ['7', '8', '9']:
                        count += 1 * f1(i + 2)
                    else:
                        count += 2 * f1(i + 2)
                # 3.3
                elif s[i] != '*' and s[i + 1] == '*':
                    if s[i] == '1':
                        count += 9 * f1(i + 2)
                    elif s[i] == '2':
                        count += 6 * f1(i + 2)
                    else:
                        count += 0
                elif s[i] == '*' and s[i + 1] == '*':
                    count += 15 * f1(i + 2)
            count = count % (1000000000 + 7)
            dp[i] = count
            return count

        # 自定向上
        def f2():
            n = len(s)
            # if i == len(s):
            #     return 1
            dp[n] = 1
            for i in range(n - 1, -1, -1):
                #
                if s[i] == '0':
                    dp[i] = 0
                    continue
                # 2
                if s[i] == '*':
                    dp[i] = 9 * dp[i + 1]
                else:
                    dp[i] = 1 * dp[i + 1]
                # 3.1
                if i + 1 <= len(s) - 1:
                    if s[i] != '*' and s[i + 1] != '*':
                        if int(s[i] + s[i + 1]) > 26:
                            dp[i] += 0
                        else:
                            dp[i] += 1 * dp[i + 2]
                    # 3.2
                    elif s[i] == '*' and s[i + 1] != '*':
                        if s[i + 1] in ['7', '8', '9']:
                            dp[i] += 1 * dp[i + 2]
                        else:
                            dp[i] += 2 * dp[i + 2]
                    # 3.3
                    elif s[i] != '*' and s[i + 1] == '*':
                        if s[i] == '1':
                            dp[i] += 9 * dp[i + 2]
                        elif s[i] == '2':
                            dp[i] += 6 * dp[i + 2]
                        else:
                            dp[i] += 0
                    elif s[i] == '*' and s[i + 1] == '*':
                        dp[i] += 15 * dp[i + 2]
                dp[i] %= (1000000000 + 7)
            return dp[0] % (1000000000 + 7)

        # return f1(0)%(1000000000+7)
        return f2()
