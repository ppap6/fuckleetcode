'''
给定一个整数数组 nums ，
找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_, max_ = nums[0], nums[0]
        for i in nums[1:]:
            sum_ = sum_ + i if sum_ > 0 else i
            max_ = max_ if max_ > sum_ else sum_
        return  max_

a = [-2,1]
b = Solution()
print(b.maxSubArray(a))