#leetcode 78
#取得所有的子序列(去重的)
#"abc" O（n*2^n）时间复杂度
class Solution(object):
    def subsets(self, nums):
        set_str = set()
        path = []
        self.f1(nums, 0, path, set_str)
        ans = []
        for p in set_str:  # 使用不同的变量名避免覆盖
            ans.append(list(p))  # 将 tuple 转换为 list
        return ans

    def f1(self, nums, i, path, set_str):
        # 到达递归终点时
        if i == len(nums):
            # 将 path 转换为 tuple 再加入 set，确保 path 不可变
            set_str.add(tuple(path))
        else:
            # 包含当前元素
            path.append(nums[i])
            self.f1(nums, i + 1, path, set_str)
            # 回溯
            path.pop()

            # 不包含当前元素
            self.f1(nums, i + 1, path, set_str)

if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1,2,3]))
