'''
一个长度为n-1的递增排序数组中的所有数字都是唯一的，
并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

输入: [0,1,2,3,4,5,6,7,9]
输出: 8
'''
# 归类：二分法

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        if nums[right] == right:return right+1
        while left < right:
            mid = (right-left) // 2 + left
            if mid != nums[mid]:
                # 前半段缺失
                right = mid
            else:
                # 后半段缺失
                left = mid + 1
        return nums[right]-1

# 优化：
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m: i = m + 1
            else: j = m - 1
        return i
