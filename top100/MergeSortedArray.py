#88
#合并排序数组
class Solution:
    def merge(self, nums1, m, nums2, n):
        i = 0
        j = 0
        merged = []
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        merged.append(nums1[i:])
        merged.extend(nums2[j:])
        return merged