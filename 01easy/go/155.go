package easy

type MinStack struct {
	d    []int
	minD []int
	top  int
}

/** initialize your data structure here. */
/** 这种算法可以调整初始化切片的大小来调整速度/内存占用, 如将d,minD初始化为1000会更快**/
func Constructor() MinStack {
	d := make([]int, 10)
	minD := make([]int, 10)
	return MinStack{
		d:    d,
		minD: minD,
		top:  0,
	}
}


func (this *MinStack) Push(x int) {
	if len(this.d) > this.top-1 { // 栈满
		this.d = append(this.d, 0)
		this.minD = append(this.minD, 0)
	}
	if this.top == 0 { // 空栈
		this.minD[this.top] = x
	} else {
		min := this.minD[this.top-1]
		if x < min {
			this.minD[this.top] = x
		} else {
			this.minD[this.top] = min
		}
	}
	this.d[this.top] = x
	this.top++
}

func (this *MinStack) Pop() {
	if this.top == 0 {
		return
	}

	this.top--
}

func (this *MinStack) Top() int {
	// 这里假设操作总是在 非空栈 上调用
	return this.d[this.top-1]
}

func (this *MinStack) GetMin() int {
	return this.minD[this.top-1]
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
