#22
#LeetCode 的第 22 题是 "Generate Parentheses"，
#要求是生成所有可能的并且有效的括号组合。这个题目的关键是使用回溯法来生成正确的括号序列。
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def f1(str, left, right):#str是已有序列，left说明有几个左括号，right指已有几个右括号
            if 2*n == len(str):
                ans.append(str)
                return
            if left < n:
                f1(str+"(", left+1, right)
            if right < left:
                f1(str+")", left, right+1)

        f1("", 0, 0)
        return ans

