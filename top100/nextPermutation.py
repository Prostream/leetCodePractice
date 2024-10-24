#31
#要求对给定数组找出数学上的下一个更大的排列。如果这样的排列不存在
# （即数组已经是按照从大到小的顺序排列），
# 则必须重置为最小排列（即按照从小到大的顺序排列
#
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i <= 0:
            nums.reverse()
            return
        j = len(nums) - 1
        while nums[j] <= nums[i - 1]:
            j -= 1
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        nums[i:] = reversed(nums[i:])