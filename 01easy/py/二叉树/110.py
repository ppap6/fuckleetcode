'''
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

'''

# 执行用时：96 ms，内存消耗：17.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None: return True
        return abs(self.find_deep(root.left) - self.find_deep(root.right)) <= 1 and self.isBalanced(
            root.left) and self.isBalanced(root.right)

    def find_deep(self, node):
        return max(self.find_deep(node.left) + 1, self.find_deep(node.right) + 1) if node is not None else 0