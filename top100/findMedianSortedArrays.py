#4
#
#Input: nums1 = [1,3], nums2 = [2]
#Output: 2.00000
#Explanation: merged array = [1,2,3] and median is 2.
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #i 作为nums1的中点
        #m+n+1//2 - i作为nums2的中点
        #保证nums1[i-1]<nums2[m+2+1//2 - i]
        #nums[i]>nums[m+2+1//2 - i - 1
        # 确保 nums1 是较短的数组
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        imin, imax = 0, m
        half_len = (m + n + 1) // 2

        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i

            # i 太小，说明划分点在右边，需要右移 i
            if i < m and nums2[j - 1] > nums1[i]:
                imin = i + 1
            # i 太大，说明划分点在左边，需要左移 i
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            # 找到合适的划分点
            else:
                # 计算左半部分的最大值
                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                # 如果总长度是奇数，直接返回左半部分的最大值
                if (m + n) % 2 == 1:
                    return max_of_left

                # 计算右半部分的最小值
                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                # 如果总长度是偶数，返回左右两部分的平均值
                return (max_of_left + min_of_right) / 2.0

if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1,2],[3,4]))
