'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
输入：n = 7
输出：21

输入：n = 2
输出：2
'''
# 归类; 动态规划

class Solution:
    def numWays(self, n: int) -> int:
        if n<=1: return 1
        if n ==2: return 2
        dp = [0] * (n+1)
        dp[0],dp[1],dp[2] = 1,1,2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]%1000000007