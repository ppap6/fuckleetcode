'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
         n = len(nums)/2
         d = {}
         for key in nums:
             d[key] = d.get(key,0)+1
         for k,v in d.items():
             if v>n:return k