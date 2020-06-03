'''
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，
A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。
'''


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        d = {}
        for i in nums:
            d[i]=d.get(i,0)+1
        tmp = d.get(0,0) # 0的个数
        for i in range(tmp+1,len(nums)):
            if nums[i]-nums[i-1] > (tmp+1) or nums[i]- nums[i-1]==0:
                return False
            else:
                n = nums[i]-nums[i-1]-1
                tmp -= n
        return True if tmp>=0 else False

