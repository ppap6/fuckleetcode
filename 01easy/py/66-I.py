'''
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

'''


# 硬解
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = 0
        for n in range(len(digits)-1,-1,-1):
            if n == len(digits)-1:
                digits[n] += 1+flag
            digits[n] += flag
            if digits[n] >= 10:
                flag = 1
                digits[n] = digits[n]%10
                if n ==0:
                    digits.insert(0,1)
            else:
                flag = 0
        return digits