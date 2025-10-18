#2592题，田忌赛马，把 nums 重新排列成 perm，伟大值是满足 perm[i] > nums[i] 的下标个数，求最大值。
#双指针
from typing import List


class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        perm = sorted(nums)
        p1 = p2 = 0
        n = len(nums)
        ans = 0
        # [1,1,1,2,3,3,5]
        # [1,1,1,2,3,3,5]
        while p1 < n and p2 < n:
            if perm[p1] < perm[p2]:
                p1 += 1
                p2 += 1
                ans += 1
            else:
                p2 += 1

        return ans