'''
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left, right = self.maxDepth(root.left), self.maxDepth(root.right)
        print(left, "|",right)
        return max(left,right) + 1

class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1) if root is not None else 0