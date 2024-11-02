#264 质子为2，3，5就是丑数
#返回第n个丑数
#准备三个指针,如果有指针的值被选为了下一个丑数，这个指针前进一步
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = {}
        p2 = 1
        p3 = 1
        p5 = 1
        dp[1] = 1#第一个丑数是1
        for i in range(2, n+1):
            a = dp[p2] * 2
            b = dp[p3] * 3
            c = dp[p5] * 5
            cur = min(a, b, c)
            if cur == a:
                p2 += 1
            if cur == b:
                p3 += 1
            if cur == c:
                p5 += 1
            dp[i] = cur
        return dp[n]

