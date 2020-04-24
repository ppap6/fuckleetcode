package easy

// ref: https://leetcode-cn.com/problems/valid-parentheses/

// 用slice模拟栈
// 用last表示栈顶
func IsValid(s string) bool {
	last := 0
	d := map[string]string{")":"(", "}": "{", "]": "["}
	stack := make([]string, len(s))

	for _, sv := range s {
		v := string(sv)
		if v == "}" || v == "]" || v == ")" {
			if last == 0 {
				return false
			}
			if d[v] != stack[last-1] {
				return false
			}
			last -= 1
		} else {
			stack[last] = v
			last += 1
		}
	}

	return last == 0
}
