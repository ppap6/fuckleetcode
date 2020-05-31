'''
给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:return True
        def mirror_tree(node1,node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False
            return all([mirror_tree(node1.left, node2.right), mirror_tree(node1.right,node2.left)])
        return mirror_tree(root.left, root.right)