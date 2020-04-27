'''假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O(log n) 级别。
'''
# 解题思路：二分法，mid位置元素一定处于有序区间里，
# 再与首（或尾）元素比较即可知道那一段为有序
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:# 注意列表为空的时候
            return -1

        left = 0
        right = len(nums) - 1
        while left < right:

            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return mid

            if nums[left] < nums[mid]:  # 左边有序
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:  # 右边有序
                if nums[mid + 1] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid

        return left if nums[left] == target else -1

    # 解法二：
    class Solution:
        def search(self, nums: List[int], target: int) -> int:
            try:
                return nums.index(target)
            except:
                return -1