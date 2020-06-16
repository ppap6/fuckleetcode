'''
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
'''

# 此处用了三个指针，tmp初始有序列表nums1最大的数，p1初始nums的end位置, p1初始nums2的end位置
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 用的内置方法
        # while n>0:
        #     nums1.pop()
        #     n -=1
        # nums1.extend(nums2)
        # nums1.sort()

        # 算法实现
        tmp = m - 1
        p1 = m + n - 1
        p2 = n - 1
        while p2 >= 0 and tmp >= 0:
            if nums2[p2] >= nums1[tmp]:
                nums1[p1] = nums2[p2]
                p2 -= 1
            else:
                nums1[p1] = nums1[tmp]
                tmp -= 1
            p1 -= 1
        nums1[:p2 + 1] = nums2[:p2 + 1]