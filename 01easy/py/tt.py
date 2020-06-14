# 一个十进制整数转换任意进制的数
import math
def ten_to_other(nums, n:int):
    '''
    :param nums: 一个十进制数
    :param n: 要转化的进制
    :return res: 以转换进制显示的字符串
    '''
    integer = float(nums)
    tmp1, tmp2, i = "", "", 10
    if "." in nums:
        stack = nums.split(".")
        integer, decimal = int(stack[0]), float(stack[1])/ pow(10,len(stack[1]))
        tmp2 += str(int(decimal * n ))
        decimal = decimal * n - int(decimal * n)
        while decimal  != int(decimal) and i>1:
            tmp2 += str(int(decimal * n))
            decimal = decimal * n - int(decimal * n)
            i -= 1
    while integer:
            tmp1 += str(integer % n)
            integer = integer // n
    return tmp1[::-1]+"."+tmp2 if tmp1 else "0."+tmp2

# 十进制整数转换任意进制的数（不包含小数部分）
def baseN(num, b):
    return ((num == 0) and "0") or (baseN(num // b, b).lstrip("0") + "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"[num % b])


# 任意进制的数转化为十进制的数（含小数）
def other_to_ten(s:str, n:int):
    baseList = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    '''
    :param s: 一个字符串
    :param n: 该字符窜的进制
    :return res: 十进制数
    '''
    integer = s
    res1, res2 = 0, 0
    if '.' in s:
        stack = s.split(".")
        integer, decimal = stack[0], stack[1]
        for index, v in zip(range(-1, -len(decimal) - 1, -1), decimal):
            if baseList.index(v) >= n: return "error"
            res2 += baseList.index(v) * (n ** index)
    for index, v in zip(range(len(integer)),integer[::-1]):
        if baseList.index(v) >=n: return "error"
        res1 += baseList.index(v)*(n**index)
    return res1+res2

print(other_to_ten("1101.1", 2))
print(ten_to_other("13.5", 2))
# print(baseN(16, 16))