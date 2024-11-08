#238
#求数列nums[i]除了i位置以外元素的乘积，不能超过o(n)，不能使用除法
#维护每个位置的左右乘积，两个array
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 计算
        n = len(nums)
        answer = [1] * n

        # 计算左侧所有元素的乘积
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        # 计算右侧所有元素的乘积并乘以左侧的结果
        R = 1
        for i in reversed(range(n)):
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer



