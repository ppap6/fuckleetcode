package medium

// ref: https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	if n <= 0 {
		return head
	}

	// 找到倒数第n个节点间的前一个节点， 即slow节点
	slow, fast := head, head
	for i := 0; i <= n; i++ {
		if fast == nil { // n = 链表长度的情况 eg head = [1, 2] n=2
			return head.Next
		}
		fast = fast.Next
	}

	for fast != nil {
		fast = fast.Next
		slow = slow.Next
	}

	// 删除倒数第n个节点
	slow.Next = slow.Next.Next
	return head
}


