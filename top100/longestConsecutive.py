#128
#找到一个未排序数组中最长的连续序列1234这样
#先把数组放进hashtable里，n复杂度；
# 然后遍历数组，看看num-1有没有
# 如果有，说明这个num不是起点
# 如果没有，说明是起点，开始找它的后续num+1，num+2，加到没法加，然后看看和最长的比有没有更长
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #dict = {}#key是nums的元素，value是index
        dict = set(nums)
        max_len = 0
        # for i in range(len(nums)):
        #     dict[nums[i]] = i
        for num in dict:#这里用hashset效率高一点
            if num-1 not in dict:#说明是起点
                length = 1#num必定在
                start = num
                while start+1 in dict:
                    length += 1
                    start = start+1
                if length > max_len:
                    max_len = length
        return max_len

if __name__ == '__main__':
    s = Solution()
    print(s.longestConsecutive([100,4,200,1,3,2]))