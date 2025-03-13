import sys


def find_nearest_smaller(n, arr):
    stack = []  # 单调栈
    ans = [[-1, -1] for _ in range(n)]  # 结果数组，默认值为 -1

    # 遍历阶段
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            cur = stack.pop()
            ans[cur][0] = stack[-1] if stack else -1  # 左边最近且小
            ans[cur][1] = i  # 右边最近且小
        stack.append(i)

    # 清算阶段
    while stack:
        cur = stack.pop()
        ans[cur][0] = stack[-1] if stack else -1
        ans[cur][1] = -1

    # 修正阶段（只修正右侧答案）
    for i in range(n - 2, -1, -1):
        if ans[i][1] != -1 and arr[ans[i][1]] == arr[i]:
            ans[i][1] = ans[ans[i][1]][1]

    return ans


def main():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    arr = list(map(int, input_data[1:n + 1]))

    result = find_nearest_smaller(n, arr)

    for l, r in result:
        print(l, r)


if __name__ == "__main__":
    main()
