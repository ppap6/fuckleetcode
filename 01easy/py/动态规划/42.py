'''
输入一个整型数组，数组里有正数也有负数。
数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)。

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''

# 暴力破解：
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_= nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            res += nums[i]
            if res <= 0:
                max_ = max(nums[i], max_)
                if nums[i] > 0:
                    res = nums[i]
                else:
                    res = 0
            else:
                if res < nums[i]:
                    res = nums[i]
                max_ = max(res,max_)
        return max_

# 归纳：dp
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*(len(nums))
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(nums[i], nums[i]+dp[i-1])
        return max(dp)