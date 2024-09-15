# 重点：1.双端队列（双向链表可以轻松实现） 2.存储的是index，这样可以轻易判断是否已经滑过了
# Firstly, instead of adding values to current_window,
# we use their indexes. By doing this,
# we can easily check which index has fallen out of the current window and remove it.

#每当有新的element进入，判断是否老的element需要弹出了（<=new 就需要弹出）
#同时，index如果<i-k+1也需要弹出
from collections import deque
#找到每个滑动窗口（长度w）的最大值
def find_max_sliding_window(nums, w):

    result = []
    current_window = deque()

    for i in range(len(nums)):
        if len(current_window) == 0 :
            current_window.append(i)
        # 同时，index如果<i-k+1也需要弹出
        if current_window and current_window[0] <= (i - w):
            current_window.popleft()
        # 每当有新的element进入，判断是否老的element需要弹出了（<=new 就需要弹出）
        clean_up(current_window, nums, i)
        current_window.append(i)
        if i >= w - 1:
            result.append(nums[current_window[0]])
    return result

#队列的清理操作
def clean_up(current_window, nums, i):
    while current_window and nums[i] >= nums[current_window[-1]]:
        current_window.pop()

if __name__ == '__main__':
        find_max_sliding_window([10, 6, 9, -3, 23, -1, 34, 56, 67, -1, -4, -8, -2, 9, 10, 34, 67], 3)
