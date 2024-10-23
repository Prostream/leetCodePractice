#15
#寻找数组中三个数的和为 0 的所有不重复三元组
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            # 如果当前数字大于0，则三数之和一定大于0，结束循环
            if nums[i] > 0:
                break
            # 跳过重复元素
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left = left + 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right = right - 1
                else:#==
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left = left + 1
                    right = right - 1

        return ans

