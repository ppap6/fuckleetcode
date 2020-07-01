'''
杨辉三角：
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
'''
# 正向解
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            tmp = [None] * (i+1)
            tmp[0],tmp[-1] = 1, 1
            for j in range(1, len(tmp)-1):
                tmp[j] = res[i-1][j-1] + res[i-1][j]
            res.append(tmp)
        return res