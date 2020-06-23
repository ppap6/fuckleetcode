'''

'''

# python 内置函数
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = int(a,2) +int(b,2)
        return bin(res)[2:]
# 位运算模拟加法：
'''
在第一轮计算中，answer 的最后一位是 xx 和 yy 相加之后的结果，
carry 的倒数第二位是 xx 和 yy 最后一位相加的进位。接着每一轮中，
由于 carry 是由 xx 和 yy 按位与并且左移得到的，那么最后会补零，
所以在下面计算的过程中后面的数位不受影响，
而每一轮都可以得到一个低 ii 位的答案和它向低 i + 1i+1 位的进位，
也就模拟了加法的过程。
'''
class Solution2:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]