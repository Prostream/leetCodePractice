def binary_search_rotated(nums, target):
    # low, high, mid三个指针
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        # 如果找到目标值，返回其索引
        if nums[mid] == target:
            return mid

        # 检查左半部分是否有序
        if nums[low] <= nums[mid]:
            # 判断目标值是否在左半部分范围内
            if nums[low] <= target < nums[mid]:
                high = mid - 1  # 在左半部分搜索
            else:
                low = mid + 1  # 在右半部分搜索
        # 右半部分是有序的
        else:
            # 判断目标值是否在右半部分范围内
            if nums[mid] < target <= nums[high]:
                low = mid + 1  # 在右半部分搜索
            else:
                high = mid - 1  # 在左半部分搜索

    # 未找到目标值
    return -1