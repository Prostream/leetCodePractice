#旋转数组
#通过三次翻转完成，很巧妙
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n

        #反转从left到right，闭区间
        def reverse(left,right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n-1)
        reverse(k, n-1)#
        reverse(0, k-1)

        return nums