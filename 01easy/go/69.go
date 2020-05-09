package easy

func mySqrt(x int) int {
	var res int
	for i:=0; i<=x/2; i++{
		if i*i == x {
			res =  i
			break
		}
		if i*i > x {
			res = i-1
			break
		}
	}
	return res
}

// 二分更快
func mySqrt2(x int) int {
	if x < 2 {
		return x
	}
	l, r := 1, x/2
	for r >= l {
		mid := (l + r) / 2
		if mid * mid == x {
			return mid
		}
		if mid * mid < x {
			l = mid + 1
		} else {
			r = mid - 1
		}
	}
	return r
}

