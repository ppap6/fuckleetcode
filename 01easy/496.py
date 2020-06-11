'''
给定两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。
找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。
如果不存在，对应位置输出 -1 。
'''
# 硬解：
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        for i in range(len(nums1)):
            tmp_index = nums2.index(nums1[i])+1
            while tmp_index < len(nums2):
                if nums1[i]<nums2[tmp_index]:
                    nums1[i] = nums2[tmp_index]
                    break
                tmp_index += 1
            else:
                 nums1[i] = -1
        return nums1

# 优化使用单调递减栈，以及哈希表dic
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, dic = list(), dict()
        for n in nums2:
            while len(stack) != 0 and stack[-1] < n:
                # dic存储了该位元素往右比它大的第一个元素，
                # 往右没有比它大的元素不存储。
                dic[stack.pop()] = n
            stack.append(n)
        return [dic.get(i,-1) for i in nums1]