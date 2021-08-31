# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 平衡二叉树条件：对于任一节点，左子树与右子树的深度差小于等于1。
import math
class Solution:
    def parseDepth(self, root: TreeNode):
        if root is None:
            return 0

        return max(self.parseDepth(root.left), self.parseDepth(root.right)) + 1


    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True

        dl = self.parseDepth(root.left)
        dr = self.parseDepth(root.right)

        return math.fabs(dl-dr) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
