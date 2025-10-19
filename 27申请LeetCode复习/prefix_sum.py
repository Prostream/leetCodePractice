"""前缀和模板。"""

from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        # nums   = [1, 2, 1, 4]
        # preNum = [0, 1, 3, 4, 8]
        # sum(left, right) = preNum[right + 1] - preNum[left]
        self.preNum = [0]*(len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.preNum[i] = self.preNum[i-1] + nums[i-1]

    def sumRange(self, left: int, right: int) -> int | None:
        if left > right:
            return None
        return self.preNum[right + 1] - self.preNum[left]


if __name__ == "__main__":
    nums = [2, -1, 3, 5]
    num_array = NumArray(nums)

    print(num_array.preNum)       # [0, 2, 1, 4, 9]
    print(num_array.sumRange(1, 3))  # 7
    print(num_array.sumRange(0, 0))  # 2
    print(num_array.sumRange(0, 3))  # 9
