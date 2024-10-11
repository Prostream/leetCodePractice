#88
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #3个指针，两个挂在有效数组末尾，一个挂在长数组真实末尾
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
            m, n = n, m
        pointer1 = m - 1
        pointer2 = n - 1
        p = len(nums1) - 1
        while pointer2 >= 0 and pointer1 >= 0:
            if nums1[pointer1] >= nums2[pointer2]:
                nums1[p] = nums1[pointer1]
                pointer1 = pointer1 - 1
                p -= 1
            else:
                nums1[p] = nums2[pointer2]
                pointer2 = pointer2 - 1
                p -= 1
        nums1[:pointer2 + 1] = nums2[:pointer2 + 1]
        return nums1

if __name__ == '__main__':
    print(Solution().merge([2,0], 1, [1], 1))
