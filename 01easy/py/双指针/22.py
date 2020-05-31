'''输入一个链表，输出该链表中倒数第k个节点。
为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。
这个链表的倒数第3个节点是值为4的节点。
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 解法1:双指针
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        forward= back = head
        while k :
            if forward.next:
                forward = forward.next
                k -= 1
            else:
                return head
        while forward.next:
            forward, back = forward.next, back.next
        return back.next

# 解法2：
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        curNode = head
        result = []
        n = 1
        while curNode.next:
            n += 1
            curNode = curNode.next
        if k > n: return None
        if k == n: return head
        curNode = head
        for i in range(n - k - 1):
            curNode = curNode.next
        return curNode.next

