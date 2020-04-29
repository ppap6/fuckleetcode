'''
给你一个 山脉数组 mountainArr，请你返回能够使得
 mountainArr.get(index) 等于 target 最小 的下标 index 值。
  如果不存在这样的下标 index，就请返回 -1。
'''
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        left, right = 0, mountain_arr.length()-1
        while left < right:
            mid = (right - left) // 2 + left
            if mountain_arr.get(mid) > mountain_arr.get(mid + 1):
                right = mid
            else:
                left = mid + 1
        MaxIndex = right # 最大的下标
        # 递增区域用二分法查找
        left, right = 0, MaxIndex
        while left < right:
            mid = (right - left) //2 +left
            if mountain_arr.get(mid) < target:
                left = mid + 1
            else:
                right = mid
        if mountain_arr.get(right) == target: return right
        #递减区域用二分法查找
        left, right = MaxIndex, mountain_arr.length() - 1
        while left < right:
            mid = (right - left) // 2 + left
            if mountain_arr.get(mid) > target:
                left = mid + 1
            else:
                right = mid
        return right if mountain_arr.get(right) == target else -1

