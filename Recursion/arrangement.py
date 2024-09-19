#leetcode-46 全排列
class Solution:
    def arrange(self, nums):
        res = []
        set_str = set()
        self.f(nums, 0, set_str)
        for s in set_str:
            res.append(list(s))
        return res

    #不存储多余的变量来维护path信息，而是使用nums自己
    def f(self, nums, i, set_str):
        if i == len(nums):
            set_str.add(tuple(nums))
        else:
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                self.f(nums, i + 1, set_str)
                nums[i], nums[j] = nums[j], nums[i]

if __name__ == '__main__':
    s = Solution()
    print(s.arrange([1, 2, 3]))