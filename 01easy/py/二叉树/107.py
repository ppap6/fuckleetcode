'''
给定一个二叉树，返回其节点值自底向上的 层次遍历。
（即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue = []
        cur = [root]
        while cur:
            cur_lauer_val = []
            next_layer_node = []
            for node in  cur:
                if node:
                    cur_lauer_val.append(node.val)
                    next_layer_node.extend([node.left, node.right])
            if cur_lauer_val:
                queue.insert(0, cur_lauer_val)
            cur = next_layer_node
        return queue

