package easy

// 最优解法
func backspaceCompare(S string, T string) bool {
	return equal(buildStack(S), buildStack(T))
}

func buildStack(s string) *stack {
	st := newStack()
	symbol := byte("#"[0])
	for i:=0; i<len(s); i++ {
		if s[i] == symbol{
			st.Pop()
		} else {
			st.Push(s[i])
		}
	}
	return st
}

type stack struct {
	d []byte
	top int
}

func newStack() *stack {
	var s []byte
	return &stack{
		d:   s,
		top: 0,
	}
}

func (s *stack) Push(b byte) {
	if s.Len() == len(s.d) {
		s.d = append(s.d, b)
	}
	s.d[s.top] = b
	s.top += 1
}

func (s *stack) Pop() byte{
	var r byte
	if s.top > 0 {
		r = s.d[s.top-1]
		s.top--
	}
	return r
}

func (s *stack) Len() int {
	return s.top
}

func equal(s1 *stack, s2 *stack) bool {
	l1 := s1.Len()
	l2 := s2.Len()
	if l1 != l2 {
		return false
	}
	for i:=0; i<l1; i++ {
		if s1.Pop() != s2.Pop() {
			return false
		}
	}
	return true
}