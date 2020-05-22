class Solution:
    def maxSubArray(self, nums) -> int:
        max_= nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            res += nums[i]
            if res <= 0:
                max_ = max(nums[i], max_)
                res = nums[i]
            else:
                max_ = max(res,max_)
        return max_
s = Solution()
s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])