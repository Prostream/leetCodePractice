#45
#jump game2 ，需要计算最小的跳跃次数
class Solution:
    def jumpGame(self, nums):
        max_reach = 0
        last_step = 0
        jump = 0
        for i in range(len(nums)):
            max_reach = max(max_reach, i+nums[i])
            if i == last_step:
                jump += 1
                last_step = max_reach
                if last_step >= len(nums)-1:
                    break
        return jump