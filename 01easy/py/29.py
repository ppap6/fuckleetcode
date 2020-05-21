'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
'''

# 归类：边界问题（此题考虑 左右上下边界）

class Solution:
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []
        result = []
        left,up = 0, 0
        down = len(matrix)
        right = len(matrix[0])
        while True:
            for i in range(left,right):
                result.append(matrix[up][i])
            up += 1
            if up >= down:break

            for i in range(up,down):
                result.append(matrix[i][right-1])
            right -= 1
            if right <= left: break

            for i in range(right-1,left-1,-1):
                result.append(matrix[down-1][i])
            down -= 1
            if up >= down:break

            for i in range(down-1,up-1,-1):
                result.append(matrix[i][left])
            left += 1
            if right <= left: break

        return  result
