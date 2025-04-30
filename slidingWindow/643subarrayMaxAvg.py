#找出平均数最大定长k的连续子数组，返回最大平均数
def findMaxAverage(nums, k):
    subsum = 0
    max_sum = 0
    for i in range(len(nums)):
        subsum += nums[i]
        if i >= k:
            subsum -= nums[i-k]
        max_sum = max(max_sum, subsum)

    return max_sum/k

print(findMaxAverage([1,12,-5,-6,50,3], 4))