'''
给你一个整数数组 nums
请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字）
并返回该子数组所对应的乘积。
'''

# 解决：动态规划
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        a = b = 1
        ans = float('-inf')

        for i in range(1, n + 1):
            temp = a  # 没有比较之前的最大值
            a = max(a * nums[i - 1], b * nums[i - 1], nums[i - 1])

            b = min(temp * nums[i - 1], b * nums[i - 1], nums[i - 1])

            ans = max(ans, a)

        return ans