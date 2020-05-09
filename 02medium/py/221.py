'''
# 最大正方形
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix is None:
            return 0
        maxSide = 0
        row, col = len(matrix), len(matrix[0])
        dp = [ [0]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 1:
                    if i == 0 or j == 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    maxSide = max(maxSide, dp[i][j])
        return  maxSide**2