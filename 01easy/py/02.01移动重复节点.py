'''
与82题相同
编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

示例1:
 输入：[1, 2, 3, 3, 2, 1]
 输出：[1, 2, 3]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        s = set()
        pre = None
        node = head
        while node:
            if node.val not in s:
                s.add(node.val)
                pre = node
            else:
                pre.next= node.next
            node = node.next
        return head