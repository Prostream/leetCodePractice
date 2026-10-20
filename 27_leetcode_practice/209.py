def minSubArrayLen(target: int, nums: list[int]) -> int:
    # 在这里写你的实现
	# 题意是找到，满足子数组之和，大于等于target的最小长度
    left = 0
    _sum = 0
    n = len(nums)
    min_len = float("inf")
    for r in range(n):
        _sum += nums[r]
        while _sum >= target:
            min_len = min(min_len, r-left+1)
            _sum -= nums[left]
            left += 1

    return min_len if min_len != float("inf") else 0