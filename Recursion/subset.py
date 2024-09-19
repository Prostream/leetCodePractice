#leetcode-90
#[1,1,2,2,2,3]->[[0个1，2个2，1个3]]
class Solution:
    def subsets(self, nums):
        res = []
        ans= set()
        path = []
        nums.sort()
        self.f(nums, 0, path, ans)
        for p in ans:  # 使用不同的变量名避免覆盖
            res.append(list(p))
        return res

    def f(self, nums, i, path, ans):
        #递归的尾部
        if i == len(nums):
            ans.add(tuple(path))
        else:
            #下一组选的开始
            j = i + 1
            while j < len(nums) and nums[i] == nums[j]:
                j = j + 1
            self.f(nums, j, path, ans)
            clean_count = 0
            while i < j:
                path.append(nums[i])
                clean_count += 1
                self.f(nums, j, path, ans)
                i = i + 1
            #不想用多的参数就要自己清理干净维护的变量
            for i in range(clean_count):
                path.pop()

if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1,1,2]))