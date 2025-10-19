from typing import List


# 差分数组
class Diff:
    def __init__(self, nums: List[int]):
        if nums is None or len(nums) == 0:
            return None
        self.diff = [0]*len(nums)
        self.diff[0] = nums[0]
        for i in range(1, len(nums)):
            #diff[i]是nums[i]和nums[i-1]之差
            self.diff[i] = nums[i] - nums[i-1]
    
    #increment是nums的[l,r]闭区间，都add一个值
    def increment(self, l: int, r: int, val):
        self.diff[l] += val
        if r+1 < len(self.diff):
            self.diff[r+1] -= val


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    diff = Diff(nums)

    # 给闭区间 [1, 3] 中的每个元素加 2
    diff.increment(1, 3, 2)

    # 给闭区间 [0, 2] 中的每个元素减 1
    diff.increment(0, 2, -1)

    # 将差分数组还原为原数组
    result = [0] * len(diff.diff)
    result[0] = diff.diff[0]
    for i in range(1, len(diff.diff)):
        result[i] = result[i - 1] + diff.diff[i]

    print("差分数组:", diff.diff)
    print("还原结果:", result)  # [0, 3, 4, 6, 5]
