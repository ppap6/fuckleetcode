'''
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        max_ = 0
        step = 0
        end = 0
        for i in range(len(nums)-1):
            if max_ >= i:
                max_  = max(max_, nums[i]+i)
                if i == end:
                    step += 1
                    end = max_
        return step

b =Solution()
l1 = [3,8,1,1,1,5,6]
print(b.jump(l1))