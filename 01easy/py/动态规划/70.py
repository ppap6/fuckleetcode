'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
'''

# 递归可以，但超过时间限制
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==0:
            return 1
        if n==2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)

# 动态规划
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==0: return 1
        if n==2: return 2
        dp = [0]*(n+1)
        dp[0],dp[1],dp[2] = 0, 1, 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]