def monotonicStack(arr):
    stack = []
    ans = [[-1,-1] for _ in range(len(arr))]
    n = len(arr)
    #如果维护左边是严格的单调，就要放弃右边。反之同理,这里我们假定要维护一个单调递增的单调栈，这样就是找离得近的小值
    for i in range(len(arr)):
        while stack and arr[i] <= arr[stack[-1]]:
            cur = stack.pop()
            ans[cur][0] = stack[-1] if stack else -1
            ans[cur][1] = i
        stack.append(i)

    #如果stack没清空，清空一下
    while stack:
        cur = stack.pop()
        ans[cur][0] = stack[-1] if stack else -1
        ans[cur][1] = -1

    #最后一步操作，需要把右边的值传递过来，因为可能很多值的右边是相等的值
    for i in range(n-2,-1,-1):
        if ans[i] != -1 and arr[ans[i][1]] == arr[i]:
            ans[i][1] = ans[ans[i][1]][1]

    return ans