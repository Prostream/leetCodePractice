class Solution(object):
    """
    :type days: List[int]
    :type costs: List[int]
    :rtype: int
    """

    def mincostTickets(self, days, costs):
        dp = [-1] * len(days)
        return self.f1(days, costs, 0)


    # 递归法
    def f1(self, days, costs, i):
        duration = [1, 3, 30]
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
        duration = [1, 3, 30]
        if i == len(days):
            return 0
        if dp[i] != -1:
            return dp[i]
        ans = 1000000000000
        for plan in range(0, 3):
            j = i
            while j < len(days) and days[i] + duration[plan] > days[j]:
                j = j + 1
            ans = min(ans, costs[plan] + self.f1(days, costs, j))
        dp[i] = ans
        return ans

if __name__ == '__main__':
    s = Solution()
    s.mincostTickets([1,4,6,7,8,20], [2,7,15])

