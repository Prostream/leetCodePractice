#leetcode 1
#两数之和问题，双指针法和hash法
class Solution:
    def twoSum(self, nums, target):
        map = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in map:
                return [map[complement], i]
            map[nums[i]] = i

if __name__ == '__main__':
    print(Solution().twoSum([2,7,11,15],9))