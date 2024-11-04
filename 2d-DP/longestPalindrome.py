#子序列的最长回文长度
from collections import defaultdict


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = defaultdict(int)

        # 暴力递归 从l到r的范围的最长回文是多长
        def f0(l, r):
            if r == l:
                return 1
            if r - l == 1:
                return 2 if s[l] == s[r] else 1
            if s[l] == s[r]:
                return 2 + f0(l + 1, r - 1)
            else:
                return max(f0(l + 1, r), f0(l, r - 1))

        # 记忆化

        # 从底到顶 l行，r为列，左下不要，从下到上，从左往右填入
        def f1():
            n = len(s)
            # i对l，r对j
            for i, j in zip(range(n), range(n)):
                dp[(i, j)] = 1
                if j + 1 < n:
                    dp[(i, j + 1)] = 2 if s[i] == s[j + 1] else 1
                # print(f"dp={dp}")
            i = 1
            for l in range(n - 3, -1, -1):
                for r in range(n - i, n):
                    if s[l] == s[r]:
                        dp[(l, r)] = 2 + dp[(l + 1, r - 1)]
                    else:
                        dp[(l, r)] = max(dp[(l, r - 1)], dp[(l + 1, r)])
                    # print(f"l={l},r={r}")
                # for m in range(n):
                #     print("\n")
                #     for x in range(n):
                #         print(f"{dp[(m,x)]}",end=" ")
                # print("\n")
                # print("==================")
                i += 1

            return dp[(0, n - 1)]

        # 空间优化
        def f2():
            print_stack = []
            n = len(s)
            dp = [0] * (n + 1)
            leftdown = 0
            for l in range(n - 1, -1, -1):
                dp[l] = 1
                if l + 1 < n:
                    leftdown = dp[l + 1]#这一步很关键，这一行的l+1位置，就是上一行的l位置
                    dp[l + 1] = 2 if s[l] == s[l + 1] else 1
                if l + 2 < n:
                    for r in range(l + 2, n):
                        tmp = dp[r]
                        if s[l] == s[r]:
                            # print(f"l={l} r={r} dp[r]={dp[r]} leftdown={leftdown}")
                            dp[r] = leftdown + 2
                        else:
                            dp[r] = max(dp[r - 1], dp[r])
                        leftdown = tmp

            #     print_stack.append(copy.deepcopy(dp))
            # for i in range(len(print_stack)):
            #     print(f"dp={print_stack.pop()}")

            return dp[n - 1]

        # return f0(0,len(s)-1)
        return f2()


