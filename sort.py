def selection_sort(arr):
    #O(n^2)
    n = len(arr)
    # 遍历数组的每一个位置
    for i in range(n):
        # 假设当前位置的元素是最小的
        min_index = i
        # 从当前位置的下一个元素开始，寻找更小的元素
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # 如果找到更小的元素，则交换
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def fast_sort(arr):
    #average O(nlogn) bad O(n^2)
    return arr

def heap_sort(arr):
    #average O(nlogn) bad O(nlogn)
    return arr

# 示例用法
if __name__ == "__main__":
    unsorted_list = [64, 25, 12, 22, 11]
    sorted_list = selection_sort(unsorted_list)
    print("排序后的列表:", sorted_list)
