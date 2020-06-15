'''
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 解决：记录前一个node
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        s= set()
        node = head
        pre = None
        while node:
            if node.val in s:
                pre.next = node.next
            else:
                s.add(node.val)
                pre = node
            node = node.next

        return head