#112 Path Sum
#递归的思路
class Solution:
    targetSum = 0

    def pathSum(self, root, targetSum):
        self.targetSum = targetSum
        path = []
        self.f(root, upper_sum, path)