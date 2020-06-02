'''
求 1+2+...+n ，
要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''
class Solution:
    def sumNums(self, n: int) -> int:
        return sum(range(n+1))

# 大佬的新奇思路：短路+递归
class Solution:
    def __init__(self):
        self.res = 0
    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n-1)
        self.res += n
        return self.res