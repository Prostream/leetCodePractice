#leetcode-47 全排列去重
#O(n*n!)
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
            set_j = set()
            for j in range(i, len(nums)):
                #j位置的输没有来到过i位置，才做尝试
                while nums[j] not in set_j:
                    set_j.add(nums[j])
                    nums[i], nums[j] = nums[j], nums[i]
                    self.f(nums, i + 1, set_str)
                    nums[i], nums[j] = nums[j], nums[i]

if __name__ == '__main__':
    s = Solution()
    print(s.arrange([1, 1, 3]))