package medium

import "strings"

// 滑动窗口
func LengthOfLongestSubstring(s string) int {
	i, j, max := 0, 0, 0
	l := len(s)
	for i < l && j < l {
		if !strings.Contains(s[i:j], string(s[j])) {
			if n := j-i+1; n > max {
				max = n
			}
			j++
		} else {
			i++
		}
	}

	return max
}


// 使用map来优化，但是速度更慢， 内存更大，应该是删除map元素导致的
func LengthOfLongestSubstring2(s string) int {
	i, j, max := 0, 0, 0
	l := len(s)
	set := make(map[byte]int, l)
	for i < l && j < l {
		if _, ok := set[s[j]]; !ok{
			if n := j-i+1; n > max {
				max = n
			}
			set[s[j]] = 1
			j++
		} else {
			delete(set, s[i])
			i++
		}
	}

	return max
}

// 使用map来优化， 不删除元素， 速度提升，内存变大
func LengthOfLongestSubstring3(s string) int {
	i, j, max := 0, 0, 0
	l := len(s)
	set := make(map[byte]bool, l)
	for i < l && j < l {
		if exist := set[s[j]]; !exist {
			if n := j-i+1; n > max {
				max = n
			}
			set[s[j]] = true
			j++
		} else {
			set[s[i]]=false
			i++
		}
	}

	return max
}