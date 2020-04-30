'''
编写一个算法来判断一个数 n 是不是快乐数。
「快乐数」
定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果 可以变为  1，那么这个数就是快乐数。
如果 n 是快乐数就返回 True ；不是，则返回 False 。
'''
# 解题方法：1，集合 2，慢循环
class Solution:
    def isHappy(self, n: int) -> bool:
        myset = set()
        while 1:
            li = [int(i)**2 for i in str(n)]
            n = sum(li)
            if n == 1:
                return True
            elif n in myset:
                return False
            else:
                myset.add(n)
# 方法二：
class Solution:
    def getnextN(self, n: int) -> int:
        nextN = 0
        while n != 0:
             nextN += (n % 10) ** 2
             n = n // 10
        return nextN

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.getnextN(n)
        while (fast != 1 and slow != fast):
            slow = self.getnextN(slow)
            fast = self.getnextN(fast)
        return fast == 1