#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
给定一个排序数组和一个目标值，在数组中找到目标值，
并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。
输入: [1,3,5,6], 5
输出: 2
输入: [1,3,5,6], 2
输出: 1
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target>nums[-1]:return len(nums)
        low, high = 0, len(nums)-1
        ans = -1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] >= target:
                high = mid-1
                ans = mid
            else:
                low = mid+1
        return ans