#单调队列，队列里维护一个单调递减的结构，用来记录滑动窗口的最大最小值的
from collections import deque
def monotonicQueue(arr, k):
    dq = deque()
    n = len(arr)
    ans = []
    l = 0
    for r in range(n):
        #右边界进入队列
        while dq and arr[dq[-1]] < arr[r]:
            dq.pop()
        dq.append(r)

        if dq[0] < l:
            dq.popleft()

        if r - l + 1 >= k:
            ans.append(dq[0])
            l += 1
    return ans