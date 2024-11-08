#135
#发糖果，每个小朋友至少一个，如果某个小朋友比邻居评分高，则要比邻居多
#先赋值1
#从左往右遍历，满足一次需求
#从右往左遍历，如果评分高的糖果数量不多，就+1个
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans = [0]*len(ratings)
        #从左往右遍历
        for i in range(1,len(ratings)):
            prev = ratings[i-1]
            cur = ratings[i]
            if cur > prev:
                ans[i] += 1
        for i in range(len(ratings)-2,-1,-1):
            prev = ratings[i+1]
            cur = ratings[i]
            if cur > prev and ans[i] <= ans[i+1]:
                ans[i] = ans[i+1] + 1

        sum = 0
        for num in ans:
            sum += num
        return sum