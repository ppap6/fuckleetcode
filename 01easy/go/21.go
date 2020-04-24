package easy

// ref: https://leetcode-cn.com/problems/merge-two-sorted-lists/

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	p := &ListNode{}
	head := p
	for l1 != nil && l2 != nil {
		if l1.Val <= l2.Val {
			p.Next = &ListNode{Val: l1.Val}
			l1 = l1.Next
		} else {
			p.Next = &ListNode{Val: l2.Val}
			l2 = l2.Next
		}
		p = p.Next
	}

	for l1 != nil {
		p.Next = &ListNode{Val: l1.Val}
		l1 = l1.Next
		p = p.Next
	}

	for l2 != nil {
		p.Next = &ListNode{Val: l2.Val}
		l2 = l2.Next
		p = p.Next
	}

	return head.Next
}

func mergeTwoListsWrong(l1 *ListNode, l2 *ListNode) *ListNode {
	var p *ListNode
	head := p
	for l1 != nil && l2 != nil {
		if l1.Val <= l2.Val {
			p = &ListNode{Val: l1.Val}
			l1 = l1.Next
		} else {
			p = &ListNode{Val: l2.Val}
			l2 = l2.Next
		}
		p = p.Next // 此处有问题， 此时p1.Next为nil导致p指向空节点，而上面那种写法p1.Next不为空，p指向一个新节点
	}

	for l1 != nil {
		p = &ListNode{Val: l1.Val}
		l1 = l1.Next
		p = p.Next
	}

	for l2 != nil {
		p = &ListNode{Val: l2.Val}
		l2 = l2.Next
		p = p.Next
	}

	return head
}

// 优化方案
func mergeTwoListsOptimization(l1 *ListNode, l2 *ListNode) *ListNode {
	if l1 == nil {
		return l2
	}

	if l2 == nil {
		return l1
	}
	p := &ListNode{}
	head := p
	for l1 != nil && l2 != nil {
		if l1.Val <= l2.Val {
			p.Next = l1
			l1 = l1.Next
		} else {
			p.Next = l2
			l2 = l2.Next
		}
		p = p.Next
	}

	if l1 != nil {
		p.Next = l1
	}

	if l2 != nil {
		p.Next = l2
	}

	return head.Next

}
