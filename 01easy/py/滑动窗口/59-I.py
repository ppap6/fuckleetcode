'''
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:
  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

'''

# 归类：滑动窗口

# 暴力破解
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            if i + k > n:
                break
            nums[i] = max(nums[i:i + k])

        return nums[:n - k + 1]

# 滑动窗口：
import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()#此为滑动窗口
        res = []
        n = len(nums)
        # 滑动窗口左边界range(1-k, n-k+1),有边界range(n),差值为k（即大小）
        for i, j in zip(range(1-k, n-k+1), range(n)):
            # 确保当前的deque[0](最大值)与前一个窗口无关
            # 若相等，表示此时的deque[0]是上一个窗口最大值，所以要删掉
            if i >0 and deque[0] == nums[i-1]:deque.popleft()
            # 删除deque中小于刚进来的。
            while deque and deque[-1] < nums[j]: deque.pop()
            deque.append(nums[j])
            # 形成窗口了，记录最大值c
            if i >=0: res.append(deque[0])
        return res