'''
给定一个二叉树，判断其是否是一个有效的二叉搜索树。
假设一个二叉搜索树具有如下特征：
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node, min_, max_):
            if not node: return True
            if not min_ < node.val < max_: return False
            if dfs(node.left, min_, node.val) and dfs(node.right, node.val, max_):
                return True
            else:
                return False
        return dfs(root, float("-inf"), float("inf"))