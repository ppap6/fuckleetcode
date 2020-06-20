'''
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
给定有序数组: [-10,-3,0,5,9],

示例：
一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
      0
     / \
   -3   9
   /   /
 -10  5

'''
# 搜索二叉树的中序遍历即是一个升序序列。二分法+分而治之

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def convert_to_tree(n: List[int], start: int, end: int):
            if start > end: return None
            if start == end: return TreeNode(nums[end])
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = convert_to_tree(nums, start, mid - 1)
            root.right = convert_to_tree(nums, mid + 1, end)

            return root

        return convert_to_tree(nums, 0, len(nums) - 1)