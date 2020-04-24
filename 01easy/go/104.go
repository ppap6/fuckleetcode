package easy

// ref: https://leetcode-cn.com/problems/linked-list-cycle/

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
// hash
func hasCycle(head *ListNode) bool {
	if head == nil {
		return false
	}
	m := make(map[*ListNode]int)
	for head.Next != nil {
		if _, ok := m[head]; ok {
			return true
		} else {
			m[head] = 1
		}
		head = head.Next
	}
	return false
}

// 快慢指针
func hasCycle2(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return false
	}
	slow, fast := head, head.Next.Next
	for fast != nil && fast.Next != nil {
		if fast == slow {
			return true
		}
		fast = fast.Next.Next
		slow = slow.Next
	}

	return false
}
