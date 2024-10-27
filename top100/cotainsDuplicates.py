
#219
#数组里有没有两个相同的数的距离不超过k，有返回true,没有返回false
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict_element = {} #存储x元素上一个存储的index
        for i in range(len(nums)):
            if nums[i] in dict_element:#说明找到一个出现过的
                if i - dict_element[nums[i]] <= k:
                    return True
            dict_element[nums[i]] = i
        return False

if __name__ == '__main__':
    print(Solution().containsNearbyDuplicate([1,2,3,1], 3))
