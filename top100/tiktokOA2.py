#
from functools import lru_cache


class Solution:
    def f(self, s):
        a = [ord(c) for c in s ]
        n = len(a)

        @lru_cache(maxsize=18)
        def dp(i,j):
            if i >= n: return 0
            if j > n: return float("inf")
            if i == j: return min(dp(i,i+2), dp(i,i+3))
            return max(a[i:j]) - min(a[i:j]) + dp(j,j)
        return dp(0,0)

if __name__ == '__main__':
    s = Solution()
    print(s.f("aca"))
