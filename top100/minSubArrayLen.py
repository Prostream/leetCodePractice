#209
#找到一个最小长度的连续子数组，其元素之和至少为给定的值 s
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        total_value_window = 0
        l = 0
        min_len = float("inf")
        for r in range(len(nums)):
            total_value_window += nums[r]
            while total_value_window >= target:
                min_len= min(min_len, r-l+1)
                total_value_window -= nums[l]
                l += 1
        return min_len
