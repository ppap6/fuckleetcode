'''
给定一个正整数 n，将其拆分为至少两个正整数的和，
并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
'''
# 解决：递归，或者 动态规划
class Solution:
    def integerBreak(self, n: int) -> int:
        result = 1
        if n <=3:
            return n-1
        while n>4:
            n -= 3
            result *= 3
        return n*result