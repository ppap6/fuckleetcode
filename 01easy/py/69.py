'''
实现某一整数的平方根
'''

# 使用二分法
class Solution:
    def mySqrt(self, x: int) -> int:
        result = 0
        low, high = 0, x
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                high = mid - 1

            else:
                low = mid + 1
                result = mid

        return result