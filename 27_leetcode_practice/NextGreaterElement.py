class Solution:
    def monotonicStack(self, nums):
        stack = []
        #closest left and right index of greater or smaller element
        ans = [-1, -1] * len(nums)

        for i in range(len(nums)):
            #这里的等于来限制是否严格，如果while是带着等于的，那么ans的右界就是不严格的，左边界就是严格的
            #如果要找右边更大的数，那么就需要用大的数来触发pop，那么stack本身就需要是单调递减
            while stack and nums[stack[-1]] <= nums[i]:
                cur = stack.pop()
                #ans = [[index,index],[-1,-1],[-1,-1]]
                ans[cur][1] = i
                ans[cur][0] = stack[-1] if stack else -1
            stack.append(i)

        #stack清空，把左边界的处理了
        while stack:
            cur = stack.pop()
            ans[cur][1] = -1
            ans[cur][0] = stack[-1] if stack else -1

        #因为我们的右边界是不严格的，所以会有元素的右边界的index对应的值，和元素相等
        for i in range(len(nums)-2, -1, -1):
            if ans[i][1] != -1 and nums[ans[i][1]] == nums[i]:
                ans[i][1] = ans[ans[i][1]][1]

        return ans