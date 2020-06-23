# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode):
        if root is None: return 0
        if root.left is None and root.right is None:
            return 1
        a = self.minDepth(root.left)
        b = self.minDepth(root.right)
        if root.left is None or root.right is None:
            return a + b + 1
        return min(a,b)+1

s =Solution()
# [3,9,20,null,null,15,7]
a= TreeNode(20)
a.left = TreeNode(15)
a.right = TreeNode(7)
root = TreeNode(3)
# root.left = TreeNode(9)
root.right = a
print(s.minDepth(root))