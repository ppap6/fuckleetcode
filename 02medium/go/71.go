package medium

func simplifyPath(path string) string {
	slash := byte("/"[0])
	point := byte("."[0])
	pathStack := newStack()
	for i:=0; i<len(path); i++{
		c := path[i]

		// 处理斜杠
		if c == slash {
			if pathStack.Len() == 0 {
				// 空栈，直接进栈
			} else if pathStack.Top() == slash {
				// 什么也不作
				continue
			} else if pathStack.Top() == point{
				// 去除点
				pathStack.Pop()
				continue
			}

		}

		// 处理逗号
		if c == point {
			if pathStack.Top() == point {
				if i+1 <= len(path)-1 && path[i+1] != point { //  for /... 这个坑爹目录， 因为可以创建一个是...的目录
					pathStack.Pop()
					pathStack.Pop()
					if pathStack.Len() != 0 {
						pathStack.Pop()
					}
					continue
				}
			}

		}
		pathStack.Push(c)
	}

	var pathSlice = make([]byte, pathStack.Len())
	for i:=pathStack.Len()-1; i>=0; i-- {
		pathSlice[i] = pathStack.Pop()
	}

	result := string(pathSlice)
	if len(result) <= 1 {
		return "/"
	}
	return string(pathSlice)[:len(pathSlice)-1]
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

func (s *stack) Top() byte {
	var top byte
	if s.top >= 1 {
		top = s.d[s.top-1]
	}
	return top

}


func (s *stack) Len() int {
	return s.top
}
