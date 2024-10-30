from typing import List

#26
#把array里的重复数字去掉，应该是hash法和双指针都可以
#slow维护位置，fast去前面取数
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        slow = 0
        fast = 0
        #如果快慢指针相等，fast前进
        #如果不等，s前进，然后赋值
        #最后把slow+1返回
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1