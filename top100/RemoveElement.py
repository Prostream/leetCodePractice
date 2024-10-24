#27
#要求在给定数组中移除所有指定的值，并返回新数组的长度。题目的核心是原地修改数组元素。
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return []

        l = 0
        r = 0
        while r < len(nums):
            if nums[r] != val:#要保留的数
                nums[l] = nums[r]
                l += 1
                r += 1
            else:
                r += 1

        return l


