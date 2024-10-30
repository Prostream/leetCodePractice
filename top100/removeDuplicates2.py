#80
#变化的移除重复元素，主要是慢指针维护结果，快指针去找和结果倒数俩个任意一个不一样的元素
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        slow = 1
        fast = 2
        # 如果已经有两个元素了，fast前进
        # 遇到不一样的元素，赋值，然后一起前进
        # 最后把slow+1返回
        while fast < len(nums):
            if nums[fast] != nums[slow] or nums[fast] != nums[slow-1]:

                slow += 1
                nums[slow] = nums[fast]
                fast += 1
            else:
                fast += 1

        return slow + 1