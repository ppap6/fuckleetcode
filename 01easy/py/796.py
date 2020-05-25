'''
给定两个字符串, A 和 B。
A 的旋转操作就是将 A 最左边的字符移动到最右边。
 例如, 若 A = 'abcde'，在移动一次之后结果就是'bcdea' 。
如果在若干次旋转操作之后，A 能变成B，那么返回True。

'''

# 自己的傻逼方法：
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False
        if len(B) == 0: return True
        for i in range(len(B)):
            if B[:i + 1] in A:
                continue
            else:
                return True if B[i:] in A else False

# 一行
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return len(A)==len(B) and B in (A+A)