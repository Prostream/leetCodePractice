class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        arr = sorted(nums)
        n = len(arr)
        i = 0  # 指向"被压过"的元素
        count = 0

        # j 指向用于压过 arr[i] 的元素
        for j in range(n):
            if arr[j] > arr[i]:
                count += 1
                i += 1
                # 如果 i == n 就说明所有元素都被成功匹配过了
                if i == n:
                    break

        return count
    